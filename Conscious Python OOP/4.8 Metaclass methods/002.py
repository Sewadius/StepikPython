class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self(20))

    def __call__(self, *args, **kwargs):
        return 20 - self.age


masha = Person('Masha', 9)
vasya = Person('Vasya', 19)
