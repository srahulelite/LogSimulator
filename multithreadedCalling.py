import threading
import time

from errorMonitor import err_log_filter
from logGenerator import generate_logs

t1 = threading.Thread(target=generate_logs, daemon=True)
t2 = threading.Thread(target=err_log_filter, daemon=True)

t1.start()
time.sleep(1)  # Give some time for logs to generate before monitoring
t2.start()

t1.join()
t2.join()
