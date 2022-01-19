# This script gets an 'argv' argument, i.e: python create-file.py textfile.txt
# -and creates the argument file, if not exists, otherwise print an error.
import os
import sys

filename = sys.argv[1]
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("New File Created!\n")
else:
    print(f"Error! the file <{filename}> already exists.")
    # exit with error digit 1
    sys.exit(1)
