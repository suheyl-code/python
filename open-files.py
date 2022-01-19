file = open("README.md")
lines = file.readlines()
file.close()
# Although file is closed, 'lines' still has the info
# -in the form of a list.
print(lines)

# 'with' keyword closes the file at the end as well,
# It adds a new line everytime reads a line.
with open("README.md") as file:
    for line in file:
        print(line)

# To avoid new line added problem:
with open("README.md") as file:
    for line in file:
        print(line.strip())

# A word of caution: for large files it's better to read line by line.
# -because it can take a lot of memory to keep whole file at once in
# -a variable.
