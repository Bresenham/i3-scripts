import time
import psutil
import subprocess

iw_out = subprocess.check_output(["iw", "dev", "wlan0", "link"], universal_newlines=True).strip()

if iw_out == "Not connected.":
	print("NO WiFi")
else:
	if_start = iw_out.find("(on") + 3
	if_end = iw_out.find(")")
	wifi_dev = iw_out[if_start:if_end].strip()

	ssid_start = iw_out.find("SSID:") + 6
	ssid_end = iw_out.find("freq")
	ssid = iw_out[ssid_start:ssid_end].strip()
	
	old_sent = psutil.net_io_counters().bytes_sent
	old_recv = psutil.net_io_counters().bytes_recv

	time.sleep(1)

	sent = psutil.net_io_counters().bytes_sent - old_sent
	recv = psutil.net_io_counters().bytes_recv - old_recv

	sent = sent / 1024
	recv = recv / 1024

	print("S: {:.2f}KiB, R: {:.2f}KiB by {} @ {}".format(sent, recv, wifi_dev, ssid))
