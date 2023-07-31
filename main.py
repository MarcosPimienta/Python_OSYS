from modules import system_operations as so
from modules import system_check as sc
from modules import real_time_update as rt


def main():
    while True:
        print("\nWhat would you like to do?")
        print("0. Display OS info")
        print("1. Display system partitions")
        print("2. List files in a directory")
        print("3. Create a new directory")
        print("4. Delete a file or directory")
        print("5. Rename a file or directory")
        print("6. Display the content of a file")
        print("7. Display CPU usage")
        print("8. Display memory usage")
        print("9. Quit")
        choice = input("> ")
        if choice == "0":
            os_info = sc.get_os_info()
            for key, value in os_info.items():
                print(f"{key}: {value}")
        elif choice == "1":
            partitions = sc.get_sys_partitions()
            for partition in partitions:
                print(f"Partition {partition.device}: {partition.total} total, {partition.used} used, {partition.free} free")
        elif choice == "2":
            so.list_files()
        elif choice == "3":
            so.create_directory()
        elif choice == "4":
            so.delete_path()
        elif choice == "5":
            so.rename_path()
        elif choice == "6":
            so.read_file()
        elif choice == "7":
            rt.display_cpu_usage()
        elif choice == "8":
            rt.display_memory_usage()
        elif choice == "9":
            break  # exit the loop
        else:
            print("Invalid choice, please try again.")


# Calling the main function
if __name__ == "__main__":
    main()
