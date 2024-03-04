class Person:
    ATTRIBUTES = 'name', 'age', 'study', 'work'

    def __init__(self, *args):
        for i, el in enumerate(args):
            self.__dict__[self.ATTRIBUTES[i]] = el


id_1 = Person('Vasya', 22, 'college', 'developer')
print(id_1.__dict__)
