from modules import system_operations as so
from modules import system_check as sc
from modules import real_time_update as rt


def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. List files in a directory")
        print("2. Create a new directory")
        print("3. Delete a file or directory")
        print("4. Rename a file or directory")
        print("5. Display the content of a file")
        print("6. Display CPU usage")
        print("7. Display memory usage")
        print("8. Quit")
        choice = input("> ")

        if choice == "1":
            so.list_files()
        elif choice == "2":
            so.create_directory()
        elif choice == "3":
            so.delete_path()
        elif choice == "4":
            so.rename_path()
        elif choice == "5":
            so.read_file()
        elif choice == "6":
            rt.display_cpu_usage()
        elif choice == "7":
            rt.display_memory_usage()
        elif choice == "8":
            break  # exit the loop
        else:
            print("Invalid choice, please try again.")


# Calling the main function
if __name__ == "__main__":
    main()
