import time
import random

def generate_logs():
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

    with open("logs.txt", "a") as file:  # Open in append mode
        while True:
            level = random.choice(log_levels)
            message = random.choice(messages)
            log = f"[{level}] {message}\n"
            file.write(log)  
            file.flush()  # Ensure real-time writing
            print(f"LOG WRITTEN: {log.strip()}")  # Debugging
            time.sleep(1)  # Simulate log delay

# Run this in a separate thread or process
generate_logs()