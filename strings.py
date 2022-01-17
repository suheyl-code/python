text = "This is a string literal"
# Accessing in reverse mode
print(text[-2])
# from begining to 4th
print(text[:4])

# Some useful functions
print('12345'.isnumeric())

print('afffgf'.endswith('gf'))

print(" ".join(["This", "is", "a", "sentence!"]))
print("-".join(["This", "is", "a", "phrase!"]))

print("This is a list".split())

# Formatting functions
print(f"The base price is {8.5:.2f} and with tax is {8.5 * 1.18:.2f}")
print(f"{100:>4}  | {5.32:5.2f}")
