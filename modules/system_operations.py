import os


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
