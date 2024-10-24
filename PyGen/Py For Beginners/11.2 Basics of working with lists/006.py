# Замена цвета
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

for i, el in enumerate(rainbow):
    if el == 'Green':
        rainbow[i] = 'Зеленый'
    if el == 'Violet':
        rainbow[i] = 'Фиолетовый'

print(rainbow)
