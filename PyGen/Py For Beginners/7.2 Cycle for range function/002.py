# Последовательность чисел 2
m, n = (int(input()) for _ in '12')

if m < n:
    [print(i) for i in range(m, n + 1)]
    exit(0)

[print(i) for i in range(m, n - 1, - 1)]
