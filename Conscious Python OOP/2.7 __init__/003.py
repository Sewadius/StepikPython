class BirthDay:
    def __init__(self, present: str, color: str):
        self.present = present
        self.color = color


Masha = BirthDay('pen', 'red')
Nikita = BirthDay('t-shirt', 'red')
Lena = BirthDay('ball', 'red')

names = {'Маша': Masha, 'Никита': Nikita, 'Лена': Lena}

for k, v in names.items():
    end = '' if k == 'Никита' else 'а'
    print(f'{k} подарил{end}: {v.present}, цвета: {v.color}')
