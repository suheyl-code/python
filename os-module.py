# 'os' module is for working with Filesystem on Operating System
import os

# To remove a file, if exists:
if os.path.exists("text.txt"):
    os.rename("text.txt", "text-renamed.txt")
    os.remove("text-renamed.txt")
