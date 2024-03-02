class Holiday:
    ...


friends = Holiday()

values = {
    'name1': 'Sveta',
    'name2': 'Katya',
    'name3': 'Lena',
    'name4': 'Natasha',
    'name5': 'Leonardo DiCaprio'
}

for k in values.keys():
    friends.__setattr__(k, values.get(k))

friends.name5 = 'Jack'

for i in friends.__dict__:
    if i != 'name5':
        print(getattr(friends, i))
    elif i == 'name5' and getattr(friends, i) == 'Leonardo DiCaprio':
        raise AttributeError('Машенька хочет увидеть вас на ДР')
