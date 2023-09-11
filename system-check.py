import psutil
import tkinter as tk
from tkinter import ttk

# Retrieve system info

def get_system_info():
  cpu_percent = psutil.cpu_percent(interval=1)
  ram = psutil.virtual_memory()
  ram_percent = ram.percent
  disk = psutil.disk_usage('/')
  disk_percent = disk.percent
  return cpu_percent, ram_percent, disk_percent


def refresh():
  cpu, ram, disk = get_system_info()
  cpu_var.set(f"CPU Usage: {cpu}%")
  ram_var.set(f"RAM Usage: {ram}%")
  disk_var.set(f"Disk Usage: {disk}%")

# set a delay for the next refresh

  root.after(5000, refresh) #Refresh every 5 seconds


# Create the main window
root = tk.Tk()
root.title("PC System Health Monitor")

# Variables to store current values
cpu_var = tk.StringVar()
ram_var = tk.StringVar()
disk_var = tk.StringVar()

# Create and pack Labels
ttk.Label(root, textvariable=cpu_var).pack(pady=20)
ttk.Label(root, textvariable=ram_var).pack(pady=20)
ttk.Label(root, textvariable=disk_var).pack(pady=20)

# Trigger the first data fetch
refresh()
root.mainloop()
