# Соотношение
n = int(input())
a, b, c, d = n // 1000, n // 100 % 10, n // 10 % 10, n % 10

print('ДА' if a + d == b - c else 'НЕТ')
