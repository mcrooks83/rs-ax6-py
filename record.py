
import sys
import time
from datetime import datetime
from py_lib import libomapi as api

# mimic of record.c example
# goal is to be able to provide configuration settings and setup the device to record


# Device callback
@api.OmDeviceCallback
def device_callback(ref, deviceId, status):
    if status == api.OM_DEVICE_CONNECTED:
        print("OMDEVICE: CONNECTED: " + str(deviceId))
    elif status == api.OM_DEVICE_DISCONNECTED:
        print("OMDEVICE: DISCONNECTED: " + str(deviceId))

# Log callback
@api.OmLogCallback
def log_callback(ref, message):
    print("OMLOG: " + message)


# configuration times -> python dict?
#int startDays = 1, startHour = 0;
#int durationDays = 8, endHour = 0;
#int minBatt = 85;
#int debugMode = 0;
            
#The pairing of session identifiers and their assigned device identifiers is written to an output file (if specified).
# outfile ->  not sure what this is?

# pass more properties in here like start_day etc
def record_setup(device_id, now_time):

    session_id = 1
   
    range = 8 # default range of acclerometer OM_ACCEL_DEFAULT_RANGE
    rate = 100 # default sampling rate OM_ACCEL_DEFAULT_RATE
    
    result = api.set_now_time(device_id, now_time)
    print("set time:", result)

    # check for gryo
    has_gyro = api.has_gyro(device_id)
    print("has gyro?", has_gyro)
    if(has_gyro):
        range |= 2000 << 16
        #print(range)
   
    # set the accelerometer (+gyro) configuration
    result = api.set_accel_config(device_id, rate, range)
    print("accel config", result)

    # set the session id
    print(f"setting session {session_id}")
    result = api.set_session_id(device_id, session_id)
    print("session set", result)
    
    # clear the max samples setting
    api.clear_max_samples(device_id)
    # clear the meta data
    api.clear_meta_data(device_id)

    return True

# configures connected devices
def configure_devices_to_record():

    min_batt_level = 85 # default min battery level to start a long recording

    now = datetime.now()
    now_time = datetime(
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute,
            now.second
    )

    # 1. set the device callbacks
    log_callback_set = api.set_log_callback(log_callback)
    print("log callback set", log_callback_set)

    is_callback_set = api.set_device_callback(device_callback)
    print("is callback set:", is_callback_set)

    # 2. start the library api result = OmStartup(OM_VERSION);
    result = api.start_up() # returns 0 
    print("api started")

    # 3. get the connected devices (assumes that there are devices attached via usb already)
    num_devices = api.get_num_of_connected_devices()
    if(num_devices==0):
         print(f"No Devices Found")
    else:
        print("Number of devices attached", num_devices)
        if(num_devices > 0):
            device_ids = api.get_device_ids(num_devices)
            print("device IDs", device_ids)

        # 4. loop over each device, do checks and write settings
        for idx, d_id in enumerate(device_ids):
            
            # check battery status
            batt_level = api.get_battery_level(d_id)
            print(f"battery level for device {d_id} {batt_level}")
            if(batt_level > min_batt_level):
                print("battery level at acceptable level")
                result = record_setup(d_id, now_time)
                if(result):
                    pass
                    # setup was successful
                    # set delays if any (i.e start recoding 1 day later until 8 days)
                    
                    # api set_start_recording(start_day, start_hour) returns start_time
                    # api set_stop_recording(stop_day, stop_hour) return stop_time (stop_day is now to duration)
                    # api set_delays(device_id, start_time, stop_time)

                    # commit the settings to the device
                    # resut  = commit_recording_settings(device_id)



        # 5. sleep for 5 seconds
        time.sleep(5)


# main entry point
def main(argv=None):
    if argv is None:
        argv = sys.argv

    # pass in config parameters here (user generated)
    # session id (int)
    # range / rate
    # delay info - start_day (number of days from now) start_hour () duration_days

    configure_devices_to_record()

    return 0
if __name__ == "__main__":
    sys.exit(main())