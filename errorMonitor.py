# import time
# import sys

# def err_log_filter():
#     with open("logs.txt", "r") as file:
#         file.seek(0, 2)
#         while True:
#             line = file.readline()
            
#             if not line:
#                 time.sleep(1)
#                 # print("waiting for input")
#             if "ERROR" in line:
#                 print(f"Error Log Detected - {line.strip()}", flush=True)
            # sys.stdout.flush()  # Ensure immediate outpu

import time
import os

def err_log_filter():
    with open("logs.txt", "r") as file:
        file.seek(0, os.SEEK_END)  # Move to end of file to avoid old logs
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)  # Prevent CPU overuse
                continue  # No new log, keep waiting
            if "ERROR" in line:
                print(f"⚠️ ERROR LOG DETECTED: {line.strip()}", flush=True)

