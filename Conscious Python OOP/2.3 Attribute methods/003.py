list_person = ['hobby', 'work', 'study']

class Person:
    hobby = 'dance'
    work = 'design'
    study = 'college'


id_1 = Person()
[print(getattr(id_1, el)) for el in list_person]
