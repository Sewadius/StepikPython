# Неравенство треугольника
lst = sorted([int(input()) for _ in range(3)])
print('YES' if lst[0] + lst[1] > lst[-1] else 'NO')
