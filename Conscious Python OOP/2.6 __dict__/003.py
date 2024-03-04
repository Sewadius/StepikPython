class Person:
    pass


person_1 = Person()
person_1.__dict__ = {'name': 'Vasya', 'age': '20', 'work': 'driver'}
[print(person_1.__dict__.get(key)) for key in person_1.__dict__]
