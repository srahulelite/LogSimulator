import time

def err_log_filter():
    with open("logs.txt", "r") as file:
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                # print("waiting for input")
            if "ERROR" in line:
                print(f"Error Log Detected - {line.strip()}")

err_log_filter()