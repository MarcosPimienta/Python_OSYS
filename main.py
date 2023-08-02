from rich.console import Console
from rich.table import Table
from modules import system_operations as so
from modules import system_check as sc
from modules import real_time_update as rt

console = Console()  # create a Console instance


def print_dict_as_table(data_dict):
    table = Table(show_header=True, header_style="bold green")
    for key, value in data_dict.items():
        table.add_row(key, str(value))
    console.print(table)


def main():
    # Define the dictionary that acts as a switch case
    switcher = {
        '0': lambda: print_dict_as_table(sc.get_os_info()),
        '1': lambda: print_dict_as_table(sc.get_sys_partitions()),
        '2': so.list_files,
        '3': so.create_directory,
        '4': so.delete_path,
        '5': so.rename_path,
        '6': so.read_file,
        '7': rt.display_cpu_usage,
        '8': rt.display_memory_usage,
        '9': lambda: so.execute_shell_command(input("Enter a shell command to execute: ")),
        '10': so.organize_files,
        '11': exit  # this will break the loop and exit the program
    }

    while True:
        console.print("\nWhat would you like to do?", style="bold blue")
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
            "Organize Files by Type",
            "Quit"
        ]
        table = Table(show_header=True, header_style="bold magenta")
        for i, action in enumerate(actions):
            table.add_row(str(i), action)

        console.print(table)
        choice = input("> ")

        # Get the function from switcher dictionary
        func = switcher.get(choice, lambda: console.print("Invalid choice, please try again.", style="bold red"))

        # Execute the function
        func()


# Calling the main function
if __name__ == "__main__":
    main()
