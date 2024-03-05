class Person:
    def __getattr__(self, item):
        if item == 'name':
            self.name = 'Vasya'
            return self.name
        return 'Такого атрибута нет'


person = Person()
print(person.name)
