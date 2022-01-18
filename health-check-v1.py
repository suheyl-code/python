"""
v1.0: A script to check disk usage and cpu usage.
if disk has more than 20 percent free and cpu less
than %75 active, return OK!
"""
import shutil
import psutil


def check_disk_usage(drive):
    du = shutil.disk_usage(drive)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage < 75


if not check_disk_usage("C:") or not check_cpu_usage():
    print("Error!")
else:
    print("Everything looks OK!")
