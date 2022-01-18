import shutil
# Under Linux ... ("/") root directory
du = shutil.disk_usage("C:")
print(du)
print("Free: %" + str(du.free/du.total*100))
