animals = ["Lion", "Zebra", "Monkey", "Dolphin"]

chars = 0
for animal in animals:
    chars += len(animal)

print(
    f"Total Characters in {animals}: {chars} / average length: {chars/len(animals)}")


# enumeration
for index, animal in enumerate(animals):
    print(f"{index + 1}: {animal}")


# list comprehension
result1 = []
for x in range(1, 11):
    result1.append(x*7)

# But better with list comprehension
result2 = [x*7 for x in range(1, 11)]

print(result1, result2)

languages = ['Ruby', 'Python', 'C', 'C#', 'C++', 'Javascript']
x = [len(language) for language in languages]
print(x)

odd = [ number for number in range(0,101) if number % 3 == 0]
print(odd, type(odd))
