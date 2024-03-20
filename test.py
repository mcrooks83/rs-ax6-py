import sys

from lib import libomapi as api
import time


#static void deviceCallback(void *reference, int deviceId, OM_DEVICE_STATUS status)

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

# test a connected device
def test_device(device_id):
    print(f"testing device {device_id}")

    result = api.set_led(device_id, api.LED_BLUE)
    if(result == 0):
        print(f"Led set to blue for {device_id}")
        print(f"Sleeping for 2 seconds")
        time.sleep(2)
        result = api.set_led(device_id, api.LED_WHITE)
        print(f"reset led to white for {device_id}")
	
    # get battery health
    batt_level = api.get_battery_level(device_id)
    print(f"battery level for device {device_id} {batt_level}")

    # accelerometer 
    accelerometer = api.get_accelermoter(device_id)
    print(f"accel data",accelerometer)

    #memory health
    result = api.get_memory_health(device_id)
    print(f"memory health", result)

# set up for testing
def test():

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
            print(f"testing device {idx} {id}")
            test_device(id)

    #shut down
    result = api.shut_down()
    print(result)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    test()

    return 0


if __name__ == "__main__":
    sys.exit(main())