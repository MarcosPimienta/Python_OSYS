# Python_OSYS
![DevOps-Lifecycle](https://github.com/MarcosPimienta/Python_OSYS/assets/60362847/058b50cb-c53a-4ee5-8c61-9375327fa819)

This applicatio![Uploading PyFinity.png…]()
n provides a simple command-line interface to interact with the system. It's written in Python, using standard libraries `os`, `sys`, `platform`, and `psutil` to interact with the system and gather information.

## Features

The application provides the following functionalities:

1. **System Information**: Display basic system information including OS details, virtual memory status, system uptime, and disk partition information.
2. **File Management**: Perform basic file and directory operations like listing all files and directories in a specified path, creating a new directory, deleting a file/directory, renaming a file/directory, and displaying the content of a file.
3. **Real-time System Status**: Monitor real-time system statistics such as CPU usage and memory usage.

## Installation

### On Windows:

1. Ensure that Python 3.11 is installed on your system.
2. Clone the repository: `git clone https://github.com/MarcosPimienta/Python_OSYS.git`
3. Navigate into the project directory: `cd Python_OSYS`
4. Create a virtual environment: `py -m venv env`
5. Activate the virtual environment: `.\env\Scripts\activate`
6. Get the requirements: `pip install -r requirements.txt`
7. Run the application: `python main.py`

### On Linux:

1. Ensure that Python 3.11 is installed on your system.
2. Clone the repository: `git clone https://github.com/MarcosPimienta/Python_OSYS.git`
3. Navigate into the project directory: `cd Python_OSYS`
4. Create a virtual environment: `python3 -m venv env`
5. Activate the virtual environment: `source env/bin/activate`
6. Get the requirements: `pip install -r requirements.txt`
7. Run the application: `python main.py`

## Usage

After running `main.py`, you will be presented with a menu of operations you can perform. Enter the number of the operation you want to perform and follow the prompts.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
