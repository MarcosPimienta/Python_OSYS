import os
import sys
import platform
import psutil


def get_os_info():
    try:
        os_info = {
            'os_name': os.name,
            'os_release': platform.release(),
            'platform_system': platform.system(),
            'platform_architecture': platform.architecture()
        }
        return os_info
    except Exception as e:
        print(f"An error trying to obtain OS info: {str(e)}")
        sys.exit(1)


def get_sys_resources():
    try:
        sys_resources = {
            'virtual_memory': psutil.virtual_memory(),
            'system_uptime': psutil.boot_time()
        }
        return sys_resources
    except Exception as e:
        print(f"An error trying to obtain memory and uptime info: {str(e)}")
        sys.exit(1)


def get_sys_partitions():
    partitions = []
    try:
        for partition in psutil.disk_partitions():
            partitions.append(psutil.disk_usage(partition.mountpoint))
        return partitions
    except Exception as e:
        print(f"An error trying to obtain partition info: {str(e)}")
        sys.exit(1)
