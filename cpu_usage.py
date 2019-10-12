import psutil

values = psutil.cpu_percent(percpu=True)
ret_str = ""
for i in range(len(values)):
	ret_str += "C{}: {:5.1f}, ".format(i, values[i])
print(ret_str[:-2])
