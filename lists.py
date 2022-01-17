animals = ["Lion", "Zebra", "Monkey", "Dolphin"]

chars = 0
for animal in animals:
    chars += len(animal)

print(f"Total Characters in {animals}: {chars} / average length: {chars/len(animals)}")


for index, animal in enumerate(animals):
    print(f"{index + 1}: {animal}")