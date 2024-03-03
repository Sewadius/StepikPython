class Pokemon:
    pass


pokemons = Pokemon()
for i in 'pikachu', 'scyther', 'gyarados', 'gengar':
    setattr(pokemons, i, '')
[print(hasattr(pokemons, el)) for el in ('lapras', 'pikachu', 'alakazam')]
