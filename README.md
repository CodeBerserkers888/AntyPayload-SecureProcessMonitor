# SecureProcessMonitor

![Static Badge](https://img.shields.io/badge/DefensePayload-AntyBadUSB-green)
![GitHub Release Date](https://img.shields.io/github/release-date/Bulli77/AntyPayload-SecureProcessMonitor)

<p align="center">
  <img src="https://i.imgur.com/LZXx1Ec.png" alt="SecureProcessMonitor Logo" width="265px">
</p>

## Introduction 🥷🏻

In today's world, with the increasing number of cyber threats, protecting our computer systems has become a top priority. One of the common threats is unauthorized scripts and processes, such as keyloggers and illegal data transfers to external servers. Projects like SecureProcessMonitor address these threats by providing an effective tool to monitor and eliminate suspicious processes.

#Project Objective

SecureProcessMonitor is a Python script designed to enhance system security by monitoring and terminating suspicious processes such as powershell.exe and ftp.exe. The project aims to provide users with a tool that automatically detects and stops potentially dangerous activities before they can cause harm.

# Threats Addressed by the Project

- Keyloggers: Keyloggers are malicious software that records keystrokes, allowing cybercriminals to obtain sensitive information such as passwords and personal data. SecureProcessMonitor detects and stops keylogger processes before they can - transmit collected data.

- Unauthorized Data Transfers: Processes like ftp.exe can be used to transfer files with sensitive data to external servers. Our tool monitors and blocks such activities, preventing data leaks.

PowerShell Scripts: PowerShell is a powerful tool in Windows systems that can be used for both legitimate and malicious purposes. SecureProcessMonitor monitors and stops suspicious PowerShell scripts that could modify system settings or install malware.

# Importance of Proper Protection

Proper protection of computer systems is crucial for several reasons:

- Protection of Personal Data: In the era of GDPR and other data protection regulations, securing personal information is not only a legal obligation but also a moral one.

- Prevention of Data Leaks: Corporate and personal data can be worth a fortune on the black market. Proper protection prevents leaks that can have catastrophic financial and reputational consequences.

- Operational Security: Cyber attacks can disrupt the normal functioning of systems and organizations, leading to operational interruptions and significant financial losses.

- User and Customer Trust: Companies that can ensure high security standards build trust among their customers and users, which is key to long-term success.


SecureProcessMonitor is a project that responds to contemporary cyber threats by providing a tool to monitor and terminate suspicious processes. Proper protection of computer systems is essential in the face of increasing threats and requires the right tools and strategies to ensure data and operational security. With SecureProcessMonitor, users can feel safer knowing that their systems are protected against unauthorized activities.

## Project Description & Let's GO!

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

```plaintext
2024-06-08 12:00:00 - Started monitoring suspicious processes.
2024-06-08 12:01:00 - Killed process: powershell.exe
2024-06-08 12:05:00 - Killed process: ftp.exe
2024-06-08 12:10:00 - Stopped monitoring script.
