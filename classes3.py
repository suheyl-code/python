from turtle import color


class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


class Apple(Fruit):
    pass


James_smith = Apple("Green", "Tart")
print(James_smith.flavor)
