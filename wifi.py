import time
import psutil

old_sent = psutil.net_io_counters().bytes_sent
old_recv = psutil.net_io_counters().bytes_recv

time.sleep(1)

sent = psutil.net_io_counters().bytes_sent - old_sent
recv = psutil.net_io_counters().bytes_recv - old_recv

sent = sent / 1024
recv = recv / 1024

print("S: {:.2f}KiB, R: {:.2f}KiB".format(sent, recv))
