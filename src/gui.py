import tkinter as tk
from tkinter import messagebox
import threading
from security_monitor import monitor_processes, stop_monitoring

def start_monitoring():
    thread = threading.Thread(target=monitor_processes)
    thread.start()
    messagebox.showinfo("Information", "Monitoring started")

def stop_monitoring_gui():
    stop_monitoring()
    messagebox.showinfo("Information", "Monitoring stopped")

root = tk.Tk()
root.title("SecureProcessMonitor")

start_button = tk.Button(root, text="Start Monitoring", command=start_monitoring)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Monitoring", command=stop_monitoring_gui)
stop_button.pack(pady=10)

root.mainloop()
