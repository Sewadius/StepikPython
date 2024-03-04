class Person:
    pass


vasya = Person()
vasya.__dict__.update({
    'id_1': 'Masha',
    'id_2': 'Tom Cruise',
    'id_3': 'Nicole Kidman',
    'id_4': 'Brad Pitt',
    'id_5': 'Tom Hanks',
    'id_6': 'Johnny Depp'
})

for key, value in vasya.__dict__.items():
    print(key, value)
