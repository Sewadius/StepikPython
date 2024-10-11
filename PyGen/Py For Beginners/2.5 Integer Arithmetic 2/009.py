# Четырёхзначное число
POSITION = ['тысяч', 'сотен', 'десятков', 'единиц']

n = int(input())
number = [n // 1000, n // 100 % 10, n // 10 % 10, n % 10]

for i in range(4):
    print(f'Цифра в позиции {POSITION[i]} равна {number[i]}')
