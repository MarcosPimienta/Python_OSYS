from rich.console import Console
from rich.table import Table
from modules import system_operations as so
from modules import system_check as sc
from modules import real_time_update as rt

console = Console()  # create a Console instance


def main():
    while True:
        console.print("\nWhat would you like to do?", style="bold blue")  # using console.print
        actions = [
            "Display OS info",
            "Display system partitions",
            "List files in a directory",
            "Create a new directory",
            "Delete a file or directory",
            "Rename a file or directory",
            "Display the content of a file",
            "Display CPU usage",
            "Display memory usage",
            "Execute a shell command",
            "Quit"
        ]
        table = Table(show_header=True, header_style="bold magenta")
        for i, action in enumerate(actions):
            table.add_row(str(i), action)

        console.print(table)  # print the table
        choice = input("> ")
        if choice == "0":
            os_info = sc.get_os_info()
            info_table = Table(show_header=True, header_style="bold green")
            for key, value in os_info.items():
                info_table.add_row(key, str(value))
            console.print(info_table)
        elif choice == "1":
            partitions = sc.get_sys_partitions()
            partitions_table = Table(show_header=True, header_style="bold green")
            partitions_table.add_column("Partition")
            partitions_table.add_column("Total")
            partitions_table.add_column("Used")
            partitions_table.add_column("Free")
            for partition in partitions:
                partitions_table.add_row(str(partition.device), str(partition.total), str(partition.used), str(partition.free))
            console.print(partitions_table)
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
            cmd = input("Enter a shell command to execute: ")
            so.execute_shell_command(cmd)  # execute shell command
        elif choice == "10":
            break  # exit the loop
        else:
            console.print("Invalid choice, please try again.", style="bold red")  # use colors for error messages


# Calling the main function
if __name__ == "__main__":
    main()
