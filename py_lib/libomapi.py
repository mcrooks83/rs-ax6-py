import sys

#if windows
if sys.platform == "win32":
    print("windows system")
    from c import pylibomapi_win_wrapper as omlib  # generated from demolib.h by ctypesgen
#if macos
elif sys.platform == "darwin":
    from c import pylibomapi_mac_wrapper as omlib  # generated from demolib.h by ctypesgen

import ctypes
from datetime import datetime


OM_DEVICE_CONNECTED = omlib.OM_DEVICE_CONNECTED
OM_DEVICE_DISONNECTED = 0
LED_BLUE = omlib.OM_LED_BLUE
LED_WHITE = omlib.OM_LED_WHITE
LED_RED = omlib.OM_LED_RED
LED_GREEN = omlib.OM_LED_GREEN
LED_MAGENTA = omlib.OM_LED_MAGENTA
LED_CYAN = omlib.OM_LED_CYAN

OmDeviceCallback = omlib.OmDeviceCallback
OmLogCallback = omlib.OmLogCallback


# clear device

def clear_device(device_id):
    print("CLEARING #%d: Clear data and commit...\n", device_id)
    result = omlib.OmEraseDataAndCommit(device_id, omlib.OM_ERASE_QUICKFORMAT)
    if(omlib.OM_FAILED(result)):
        print("WARNING: OmEraseDataAndCommit()", omlib.OmErrorString(result))
    return True

def clear_logging(device_id):
    print("clearing delays = <never-log>...", device_id)
    result = omlib.OmSetDelays(device_id, omlib.OM_DATETIME_INFINITE, omlib.OM_DATETIME_INFINITE)
    if (omlib.OM_FAILED(result)):
        print("WARNING: OmSetDelays()", omlib.OmErrorString(result))
    return result

def reset_accel_to_default(device_id):
    result = omlib.OmSetAccelConfig(device_id, omlib.OM_ACCEL_DEFAULT_RATE, omlib.OM_ACCEL_DEFAULT_RANGE)
    if (omlib.OM_FAILED(result)):
        print("WARNING: OmSetAccelConfig() ", omlib.OmErrorString(result))
    return result
#should probably create an API class for types as well as functions


def start_up():
    # Start the API
    print("OmStartup()")
    if omlib.OM_FAILED(omlib.OmStartup(omlib.OM_VERSION)):
        print("ERROR: OmStartup()")
        sys.exit(-1)
    else:
        return True

def set_log_callback(func):
    print("OmSetLogCallback()")
    if omlib.OM_FAILED(omlib.OmSetLogCallback(func, None)):
        print("ERROR: OmSetLogCallback()")
        sys.exit(-1)
    else:
        return True
    
def set_device_callback(func):
    # Set the device callback
    print("OmSetDeviceCallback()")
    if omlib.OM_FAILED(omlib.OmSetDeviceCallback(func, None)):
        print("ERROR: OmSetDeviceCallback()")
        sys.exit(-1)
    else:
        return True

def get_num_of_connected_devices():
    print("number of connected devices")
    result = omlib.OmGetDeviceIds(None, 0)
    if(omlib.OM_FAILED(result)):
        print(f"ERROR: OmGetDeviceIds {result}")
        return -1
    return result

def get_device_ids(num_of_devices):
    device_ids_list = [0] * num_of_devices
    device_ids = (omlib.c_int * len(device_ids_list))(*device_ids_list)
    result = omlib.OmGetDeviceIds(device_ids, num_of_devices)
   # if (OM_FAILED(result)) { printf("ERROR: OmGetDeviceIds() %s\n", OmErrorString(result)); return -1; }
    if(omlib.OM_FAILED(result)):
        print(f"ERROR OmGetDeviceIds {result}")
    if(result > 0 ):
        #turn into python list
        for idx, d in enumerate(device_ids):
            device_ids_list[idx] = d
        return device_ids_list

def set_led(device_id, color):
    #if (OM_FAILED(result)) { printf("WARNING: OmSetLed() %s\n", OmErrorString(result)); }
    if(color == omlib.OM_LED_BLUE):
        result = omlib.OmSetLed(device_id, omlib.OM_LED_BLUE)
        return result
    elif(color == omlib.OM_LED_WHITE):
        result = omlib.OmSetLed(device_id, omlib.OM_LED_WHITE)
        return result

#OmGetBatteryLevel(deviceId);
def get_battery_level(device_id):
    battery_level = omlib.OmGetBatteryLevel(device_id)
    return battery_level

def get_battery_health(device_id):
    battery_health = omlib.OmGetBatteryHealth(device_id)
    return battery_health

#OmGetAccelerometer(deviceId, &accelerometer[0], &accelerometer[1], &accelerometer[2]);
def get_accelermoter(device_id):
    accelerometer_list = [ctypes.c_int(0), ctypes.c_int(0), ctypes.c_int(0)]  # Initialize with zeros

    result = omlib.OmGetAccelerometer(device_id,
                                      ctypes.pointer(accelerometer_list[0]),
                                      ctypes.pointer(accelerometer_list[1]),
                                      ctypes.pointer(accelerometer_list[2]))
    #if (omlib.OM_FAILED(result)):
    accel = [c_int.value for c_int in accelerometer_list] 
    return accel

#OmSelfTest(deviceId);
def self_test(device_id):
    result = omlib.OmSelfTest(device_id)
    return result

#OmGetMemoryHealth(deviceId);
def get_memory_health(device_id):
    result = omlib.OmGetMemoryHealth(device_id)
    if omlib.OM_FAILED(result):
        print("WARNING: OmGetMemoryHealth() " + omlib.OmErrorString(result))
    return result

#def free_devices(device_ids):
#    omlib.free(device_ids)
#    return f"devices free"

def shut_down():
    print("shutting down api")
    result = omlib.OmShutdown()
    return result

def get_time(device_id, time):
    set_time = omlib.OM_DATETIME_FROM_YMDHMS(time.year+1900, time.month, time.day, time.hour, time.minute, time.second)
    print("RECORD #%d: TIME %04d-%02d-%02d %02d:%02d:%02d\n", device_id, time.year + 1900, time.month, time.day, time.hour, time.minute, time.second)

    return set_time

def set_delays(device_id, start_time, stop_time):
    result = omlib.OmSetDelays(device_id, start_time, stop_time)
    if (omlib.OM_FAILED(result)):
        print("ERROR: OmSetDelays()", omlib.OmErrorString(result))
        return 0
    return True

def commit_recording_settings(device_id):
    result = omlib.OmEraseDataAndCommit(device_id, omlib.OM_ERASE_WIPE)
    if (omlib.OM_FAILED(result)):
        print("ERROR: OmEraseDataAndCommit()", omlib.OmErrorString(result))
        return 0
    return result


def set_now_time(device_id, now):
    nowTime = omlib.OM_DATETIME_FROM_YMDHMS(now.year, now.month, now.day, now.hour, now.minute, now.second)
    result = omlib.OmSetTime(device_id, nowTime)
    print("set time func", result)
    #test error handling also
    if (omlib.OM_FAILED(result)): 
        print("ERROR: OmSetTime()", omlib.OmErrorString(result))
    return result

def set_accel_config(device_id, rate, range ):
    result = omlib.OmSetAccelConfig(device_id, rate, range)
    if(omlib.OM_FAILED(result)):
        print("ERROR OmSetAccelConfig", omlib.OmErrorString(result))
        return 0
    return result

def has_gyro(device_id):
    SerialBuffer = ctypes.c_char * omlib.OM_MAX_PATH  #(256)
    serial_buffer = SerialBuffer()
    if (omlib.OM_FAILED(omlib.OmGetDeviceSerial(device_id, serial_buffer))):
        return False
    result = serial_buffer[:3] == b"AX6"
    return result

def set_session_id(device_id, session_id):
    result = omlib.OmSetSessionId(device_id, session_id) #session is an unsigend int
    if(omlib.OM_FAILED(result)):
        print("ERROR OmSetSessionId", omlib.OmErrorString(result))
    return result

def set_max_samples(device_id, max):
    omlib.OmSetMaxSamples(device_id, max)

def clear_max_samples(device_id):
   print(f"clearing max samples for {device_id}")
   omlib.OmSetMaxSamples(device_id, 0)

def clear_meta_data(device_id):
    print(f"clearing meta data for {device_id}")
    omlib.OmSetMetadata(device_id, None, 0)

# def set_delays(start_day, start_hour, stop_day, stop_hour)

def set_delays(device_id, start_time, stop_time):
    result = omlib.OmSetDelays(device_id, start_time, stop_time)
    if (omlib.OM_FAILED(result)):
        print("ERROR OmSetDelays", omlib.OmErrorString(result))
        return 0
    return result

def commit_recording_settings(device_id):
    result = omlib.OmEraseDataAndCommit(device_id, omlib.OM_ERASE_WIPE)
    if (omlib.OM_FAILED(result)):
        print("ERROR OmEraseDataAndCommit", omlib.OmErrorString(result))
        return 0
    return result



### status functions

#int OmGetVersion(int deviceId, int *firmwareVersion, int *hardwareVersion

#int OmGetDeviceSerial(int deviceId, char *serialBuffer)

#int OmGetDevicePort(int deviceId, char *portBuffer)

#int OmGetDevicePath(int deviceId, char *pathBuffer)

#int OmGetTime(int deviceId, OM_DATETIME *time)

#int OmSetTime(int deviceId, OM_DATETIME time)
    
#int OmIsLocked(int deviceId, int *hasLockCode)

#int OmSetLock(int deviceId, unsigned short code)

#int OmUnlock(int deviceId, unsigned short code)

#int OmSetEcc(int deviceId, int state)

#int OmGetEcc(int deviceId)

#int OmCommand(int deviceId, const char *command, char *buffer, size_t bufferSize, const char *expected, unsigned int timeoutMs, char **parseParts, int parseMax)
