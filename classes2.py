class Dog:
    def __init__(self, name):
        self.name = name
        print(f"Dog named <{name}> created.")

    def talk(self):
        print(f"{self.name}: Can't talk, sorry!")

    def __str__(self):
        return f"This is a Dog class object <{self.name}>"


js = Dog("js")
js.talk()
print(js)   # this deals with __str__
