# logGenerator.py
import os
import random
import time
import datetime
import sys


filePath="logs.txt"

if not(os.path.exists(filePath)):
    open("logs.txt", "w").close() # create empty file

log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
messages = [
        "System running smoothly",
        "Disk space running low",
        "Connection lost",
        "Memory usage high",
        "File not found",
        "User logged in",
        "Service restarted",
    ]

def generateTimeStamp():
    ts = time.time() # TimeStamp
    return datetime.datetime.fromtimestamp(ts).strftime("[ %Y-%m-%d, %H:%M:%S ]")


with open(filePath, "a") as logfile:
    while True:
        log_content = f"{generateTimeStamp()} {random.choice(log_levels)} : {random.choice(messages)} \n"
        logfile.write(log_content)
        logfile.flush()  # Ensure real-time writing
        print(f"LOG WRITTEN: {log_content.strip()}", flush=True)  # Debugging
        # sys.stdout.flush()  # Ensure immediate output
        time.sleep(1)  # Simulate log delay

