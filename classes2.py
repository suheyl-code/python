class Dog:
    def __init__(self, name):
        self.name = name
        print(f"Dog named <{name}> created.")

    def talk(self):
        print(f"{self.name}: Can't talk, sorry!")

js = Dog("js")
js.talk()