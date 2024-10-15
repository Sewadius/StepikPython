# Цветовой микшер
COLORS = 'красный', 'синий', 'желтый'
a, b = (input() for _ in range(2))

if a not in COLORS or b not in COLORS:
    print('ошибка цвета')
    exit(0)

if a == b:
    print(a)
    exit(0)

if a == COLORS[0]:
    print('фиолетовый' if b == COLORS[1] else 'оранжевый')
if a == COLORS[1]:
    print('фиолетовый' if b == COLORS[0] else 'зеленый')
if a == COLORS[-1]:
    print('оранжевый' if b == COLORS[0] else 'зеленый')
