# Последовательность чисел 3
m, n = (int(input()) for _ in '12')
[print(i) for i in range(m, n - 1, -1) if i & 1]
