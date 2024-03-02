class Person:
    pass


id_1 = Person()
setattr(id_1, 'name', 'Vasya')
setattr(id_1, 'name', 'Masha')
print(getattr(id_1, 'name'))
