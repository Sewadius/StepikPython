# Цвета колеса рулетки
RED, BLACK, GREEN = 'красный', 'черный', 'зеленый'
n = int(input())

if n < 0 or n > 36:
    print('ошибка ввода')
    exit(0)

if not n:
    print(GREEN)
    exit(0)

check = n in range(1, 11) or n in range(19, 29)

if n & 1:
    print(RED if check else BLACK)
else:
    print(BLACK if check else RED)
