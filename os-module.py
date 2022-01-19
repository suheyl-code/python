import datetime
# 'os' module is for working with Filesystem on Operating System
import os

# Showing absolute path
print(os.path.abspath("README.txt"))

# To remove a file, if exists:
if os.path.exists("text.txt"):
    os.rename("text.txt", "text-renamed.txt")
    os.remove("text-renamed.txt")

# Get size in bytes
print(os.path.getsize("README.md"))

# shows the unix type 'timestamp' of file created time in seconds
print(os.path.getmtime("README.md"))
# to make timestamp human readable
timestamp = os.path.getmtime("README.md")
print(datetime.datetime.fromtimestamp(timestamp))
