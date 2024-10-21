# Звездный треугольник
n = int(input())
border = n // 2

for i in range(1, border + 2):
    print('*' * i)
for i in range(border, 0, -1):
    print('*' * i)
