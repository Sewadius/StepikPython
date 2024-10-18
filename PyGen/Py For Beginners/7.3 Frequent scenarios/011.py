# Последовательность Фибоначчи
a, b = (1,) * 2

for _ in range(int(input())):
    print(a, end=' ')
    a, b = b, b + a

