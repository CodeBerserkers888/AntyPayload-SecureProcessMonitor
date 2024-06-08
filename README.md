# SecureProcessMonitor

![Static Badge](https://img.shields.io/badge/DefensePayload-AntyBadUSB-green)
![GitHub Release Date](https://img.shields.io/github/release-date/Bulli77/AntyPayload-SecureProcessMonitor)

<p align="center">
  <img src="assets/logo.png" alt="SecureProcessMonitor Logo" width="200px">
</p>

## Project Description

SecureProcessMonitor is a Python script designed to enhance system security by monitoring and terminating suspicious processes such as `powershell.exe` and `ftp.exe`. The script logs events to `security_monitor.log` and provides instructions for creating an executable file.

## Project Contents

- `src/security_monitor.py`: The main script for monitoring processes.
- `src/email_notifier.py`: A script to send email notifications when a suspicious process is detected.
- `src/gui.py`: A simple GUI for starting and stopping the monitoring process.
- `requirements.txt`: A file listing the required libraries.
- `README.md`: This file with instructions.

## Installation Instructions

1. **Install Python**: Ensure Python is installed on your computer. Download it from [python.org](https://www.python.org/).

2. **Install required libraries**: Open a command prompt and run:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the script**: To start the script, navigate to the `src` directory and enter the following command in the command prompt:
    ```sh
    python security_monitor.py
    ```

## Creating an Executable File

1. **Install pyinstaller**: Open a command prompt and run:
    ```sh
    pip install pyinstaller
    ```

2. **Create the executable**: Navigate to the `src` directory and run:
    ```sh
    pyinstaller --onefile security_monitor.py
    ```

3. **Executable file**: After the process is complete, the executable file will be located in the `dist` folder. It will be named `security_monitor.exe` on Windows.

## Example Log File

An example of what the `security_monitor.log` file might look like:

```plaintext
2024-06-08 12:00:00 - Started monitoring suspicious processes.
2024-06-08 12:01:00 - Killed process: powershell.exe
2024-06-08 12:05:00 - Killed process: ftp.exe
2024-06-08 12:10:00 - Stopped monitoring script.
