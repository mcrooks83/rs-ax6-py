import sys
import time
from datetime import datetime
from py_lib import libomapi as api

# mimic of download.c - download data from all connected devices


# Callbacks

# Device callback
@api.OmDeviceCallback
def device_callback(ref, device_id, status):
    if status == api.OM_DEVICE_CONNECTED:
        print("OMDEVICE: CONNECTED: " + str(device_id))

        #result = api.set_session_id(device_id, 1)

        session_id = api.get_session_id(device_id)
        print("session id:",session_id)

        data_block_size, data_offset_blocks, data_num_blocks, start_time, end_time = api.get_data_range(device_id)
        print("data range:", data_block_size, data_offset_blocks, data_num_blocks, start_time, end_time)
        print("DOWNLOAD #%d: %d blocks data, at offset %d blocks (1 block = %d bytes)\n", device_id, data_num_blocks, data_offset_blocks, data_block_size)

        #get the start and end time to display (dont know if this actually works)
        start_string, stop_string = api.get_start_stop_string(start_time, end_time)
        print("DOWNLOAD #%d: ... %s --> %s\n", device_id, start_string, stop_string)

        if (data_num_blocks - data_offset_blocks <= 0):
            print("DOWNLOAD #%d: Ignoring - no data stored.\n", device_id)
            
        


    elif status == api.OM_DEVICE_DISONNECTED:
        print("OMDEVICE: DISCONNECTED: " + str(device_id))

# Log callback
@api.OmLogCallback
def log_callback(ref, message):
    print("OMLOG: " + message)

@api.OmDownloadCallback
def download_callback(ref, device_id, status, value):
    if (status == api.DOWNLOAD_PROGRESS):
        print("DOWNLOAD #%d: Progress %d%%.\n", device_id, value)
    
    elif(status == api.DOWNLOAD_COMPLETE):
        print("DOWNLOAD #%d: Complete.\n", device_id)
    
    elif (status == api.DOWNLOAD_CANCELLED):
        print("DOWNLOAD #%d: Cancelled.\n", device_id)
    
    elif (status == api.DOWNLOAD_ERROR):
        print("DOWNLOAD #%d: Error. (Diagnostic 0x%04x)\n", device_id, value)
    
    else:
        print("DOWNLOAD #%d: Unexpected status %d / 0x%04x\n", device_id, status, value)
    
    return


def download_data(device_id):
    pass

def download():
    # 1. set the device callbacks
    log_callback_set = api.set_log_callback(log_callback)
    print("log callback set", log_callback_set)

    is_callback_set = api.set_device_callback(device_callback)
    print("is callback set:", is_callback_set)

    download_callback_set = api.set_download_callback(download_callback)
    print("download callback set:", download_callback_set)

    # 2. start the library api result = OmStartup(OM_VERSION);
    result = api.start_up() # returns 0 
    print("api started")

    # 3. shut down
    result = api.shut_down()
    print(result)

def main(argv=None):
    if argv is None:
        argv = sys.argv

    download()

    return 0
if __name__ == "__main__":
    sys.exit(main())