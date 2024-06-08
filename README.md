# SecureProcessMonitor

![Static Badge](https://img.shields.io/badge/DefensePayload-AntyBadUSB-green)
![GitHub Release Date](https://img.shields.io/github/release-date/Bulli77/AntyPayload-SecureProcessMonitor)

<p align="center">
  <img src="https://i.imgur.com/LZXx1Ec.png" alt="SecureProcessMonitor Logo" width="256px">
</p>

## Project Description

SecureProcessMonitor is a Python script designed to enhance system security by monitoring and terminating suspicious processes such as `powershell.exe` and `ftp.exe`. The script logs events to `security_monitor.log` and provides instructions for converting the script into an executable file.

## Project Contents

- `security_monitor.py`: The main script for monitoring processes.
- `requirements.txt`: A file listing the required libraries.
- `README.md`: This file with instructions.

## Installation Instructions

1. **Install Python**: Ensure Python is installed on your computer. Download it from [python.org](https://www.python.org/).

2. **Install required libraries**: Open a command prompt and run:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the script**: To start the script, enter the following command in the command prompt:
    ```sh
    python security_monitor.py
    ```

## Creating an Executable File

1. **Install pyinstaller**: Open a command prompt and run:
    ```sh
    pip install pyinstaller
    ```

2. **Create the executable**: Navigate to the project directory and run:
    ```sh
    pyinstaller --onefile security_monitor.py
    ```

3. **Executable file**: After the process is complete, the executable file will be located in the `dist` folder. It will be named `security_monitor.exe` on Windows.

## Example Log File

An example of what the `security_monitor.log` file might look like:

