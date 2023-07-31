import os
import sys
import platform
import psutil

try:
    os_name = os.name
    os_release = platform.release()
    platform_system = platform.system()
    platform_architecture = platform.architecture()
except Exception as e:
    print(f"An error occurred when trying to obtain OS information: {str(e)}")
    sys.exit(1)

try:
    virtual_memory = psutil.virtual_memory()
    system_uptime = psutil.boot_time()
except Exception as e:
    print(f"An error occurred when trying to obtain memory and uptime information: {str(e)}")
    sys.exit(1)

partitions = []
try:
    for partition in psutil.disk_partitions():
        partitions.append(psutil.disk_usage(partition.mountpoint))
except Exception as e:
    print(f"An error occurred when trying to obtain partition information: {str(e)}")
    sys.exit(1)
