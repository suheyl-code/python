from importlib.resources import Package


class Repository:
    def __init__(self):
        self.packages = {}
        self.number = 1

    def add_package(self, package):
        self.packages[self.number] = package
        self.number += 1

    def total_size(self):
        result = 0
        for value in self.packages.values():
            result += len(value)
        return result


j = Repository()
j.add_package('jangol')
j.add_package('bipoo')
print(j.packages)
print(j.total_size())
