import sys
from py_lib import libomapi as api
import time
from datetime import datetime

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

def clear_devices():

    log_callback_set = api.set_log_callback(log_callback)
    print("log callback set", log_callback_set)

    is_set = api.set_device_callback(device_callback)
    print("is callback set:", is_set)

    result = api.start_up() # returns 0 
    print("api started",)

    num_devices = api.get_num_of_connected_devices()
    print("Number of devices attached", num_devices)

    if(num_devices==0):
         print(f"No Devices Found")
    else:
        if(num_devices > 0):
            device_ids = api.get_device_ids(num_devices)
            print("device IDs", device_ids)

        #/* For each device currently connected... */
        for idx, id in enumerate(device_ids):
            print(f"clearing device {idx} {id}")

            # set led to red
            result = api.set_led(id, api.LED_RED)

            #set session id to zero
            result = api.set_session_id(id, 0)

            # clear meta data
            result = api.clear_meta_data(id)

            # disable logging
            result = api.clear_logging(id)

            # reset accel to defaults
            result = api.reset_accel_to_default(id)

            # set time to now
            now_time = datetime.now()
            result = api.set_now_time(id, now_time)

            # clear and commit
            result = api.clear_device(id)
            
            if(result):
                print("device clearerd", result)
                result = api.set_led(id, api.LED_BLUE)
                time.sleep(2)
                api.set_led(id, api.LED_WHITE)

            

    #shut down
    result = api.shut_down()
    print(result)

def main(argv=None):
    if argv is None:
        argv = sys.argv

    clear_devices()

    return 0


if __name__ == "__main__":
    sys.exit(main())