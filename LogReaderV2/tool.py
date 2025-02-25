# tool.py
import time
import os

file_path = "logs.txt"
log_levels = {}

def process_logs():
    global log_levels

    # Open the file in read mode and move to the end
    with open(file_path, "r") as file:
        file.seek(0, os.SEEK_SET)
        while True:
            line = file.readline()
            if (not(line)):
                time.sleep(2)
                continue

            line = line.split() #spliting to get log_levels which would be at 4th index line[4]
            
            if len(line) < 4:
                continue #skip malformed lines
            else:
                print(log_levels)
                log_level = line[4]

                if(log_level in log_levels):
                    log_levels[log_level] = log_levels[log_level] + 1
                else:
                    log_levels[log_level] = 1
                
                log_levels[log_level] = log_levels.get(log_level, 0) + 1  # Fix counter
        

            # Write updated counts to stats.txt
            with open("stats.txt", "w") as stats_file:
                stats_file.write("Log Level | Count\n")
                stats_file.write("------------------\n")
                for level, count in log_levels.items():
                    stats_file.write(f"{level} \t| {count}\n")

            print(f"Updated Stats: {log_levels}")  # Debugging

process_logs()