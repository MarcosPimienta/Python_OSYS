import os
import psutil
import time


def display_cpu_usage():
    try:
        while True:
            print("CPU Usage: ", psutil.cpu_percent())
            time.sleep(1)  # wait for 1 second
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"An error occurred when trying to get CPU usage: {str(e)}")


def display_memory_usage():
    try:
        while True:
            memory = psutil.virtual_memory()
            print("Memory Usage: ", memory.percent)
            time.sleep(1)  # wait for 1 second
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"An error occurred when trying to get memory usage: {str(e)}")
