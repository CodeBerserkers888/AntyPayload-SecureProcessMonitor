import psutil
import time
from datetime import datetime
from email_notifier import notify_suspicious_process

suspicious_processes = ["powershell.exe", "ftp.exe"]
log_file = "security_monitor.log"
monitoring = True

def log_event(event):
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} - {event}\n")

def kill_process(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == process_name:
            proc.kill()
            log_event(f"Killed process: {process_name}")
            notify_suspicious_process(process_name)

def monitor_processes():
    global monitoring
    while monitoring:
        for proc_name in suspicious_processes:
            kill_process(proc_name)
        time.sleep(1)

def stop_monitoring():
    global monitoring
    monitoring = False

if __name__ == "__main__":
    try:
        log_event("Started monitoring suspicious processes.")
        monitor_processes()
    except KeyboardInterrupt:
        log_event("Stopped monitoring script.")
        print("Stopping the monitoring script.")
