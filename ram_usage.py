import psutil

d = dict(psutil.virtual_memory()._asdict())

total = d["total"] / (1024 * 1024 * 1024)
used = d["used"] / (1024 * 1024 * 1024)

print("RAM: {:.2f}/{:.2f}GiB".format(used, total))
