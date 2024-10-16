# Квадратное уравнение
a, b, c = (float(input()) for _ in '123')
d = b * b - 4 * a * c

if d < 0:
    print('Нет корней')
    exit(0)

if not d:
    print(-b / (2 * a))
    exit(0)

x1 = (-b + (b ** 2 - 4 * a * c) ** .5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** .5) / (2 * a)
print(*sorted((x1, x2)), sep='\n')
