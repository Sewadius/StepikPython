names = ['Klementina', 'Roza', 'Balu', 'Lena', 'Leonid']  # список имён


class Person:
    Vasya = ''
    Masha = ''
    Lena = ''
    Leonid = ''


[delattr(Person, el) for el in names if hasattr(Person, el)]

# строки ниже не удаляйте, ради вселенной:
print(len(Person.__dict__))
