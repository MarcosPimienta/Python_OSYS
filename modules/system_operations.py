import os
import subprocess
import shlex

def list_files():
    try:
        path = input("Enter the path: ")
        print(os.listdir(path))
    except Exception as e:
        print(f"An error occurred when trying to list files and directories: {str(e)}")


def create_directory():
    try:
        path = input("Enter the directory path to create: ")
        os.mkdir(path)
        print(f"Directory '{path}' created")
    except Exception as e:
        print(f"An error occurred when trying to create the directory: {str(e)}")


def delete_path():
    try:
        path = input("Enter the file or directory path to delete: ")
        if os.path.isfile(path):  # if it's a file
            os.remove(path)
            print(f"File '{path}' deleted")
        elif os.path.isdir(path):  # if it's a directory
            os.rmdir(path)  # only works when the directory is empty
            print(f"Directory '{path}' deleted")
    except Exception as e:
        print(f"An error occurred when trying to delete the file/directory: {str(e)}")


def rename_path():
    try:
        old_path = input("Enter the current path of the file or directory: ")
        new_path = input("Enter the new path of the file or directory: ")
        os.rename(old_path, new_path)
        print(f"Path '{old_path}' renamed to '{new_path}'")
    except Exception as e:
        print(f"An error occurred when trying to rename the file/directory: {str(e)}")


def read_file():
    try:
        file_path = input("Enter the path of the file: ")
        with open(file_path, 'r') as file:
            print(file.read())
    except Exception as e:
        print(f"An error occurred when trying to read the file: {str(e)}")


def execute_shell_command(cmd):
    """Execute a shell command and return the output"""

    # Split the command string into a list of command and arguments/flags
    flags = shlex.split(cmd)

    # Restrict dangerous commands
    danger_commands = ['rm', 'sudo', 'mkfs', 'dd']
    if any(item in danger_commands for item in flags):
        print("The command is restricted for security reasons.")
        return

    try:
        result = subprocess.run(flags, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Command output:\n{result.stdout}")
    except Exception as e:
        print(f"An error occurred while running the command: {str(e)}")
