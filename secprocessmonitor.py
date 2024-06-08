import psutil
import time
import os
from datetime import datetime

# List of suspicious processes to monitor
suspicious_processes = ["powershell.exe", "ftp.exe"]

# Log file
log_file = "security_monitor.log"

def log_event(event):
    """Writes the event to the log file""
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} - {event}")

def kill_process(process_name):
    """Kills the process with the specified name and logs the event""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == process_name:
            proc.kill()
            log_event(f "Killed process: {process_name}")

def monitor_processes():
    """Monitors running processes and kills suspicious ones""
    while True:
        for proc_name in suspicious_processes:
            kill_process(proc_name)
        time.sleep(1)

if __name__ == "__main__":
    try:
        log_event("Monitoring of suspicious processes started.")
        monitor_processes()
    except KeyboardInterrupt:
        log_event("Monitoring script stopped.")
        print("Stopped monitoring script.")
