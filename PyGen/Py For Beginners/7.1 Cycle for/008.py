# Популяция
m, p, n = (int(input()) for _ in '123')
current = float(m)

for i in range(1, n + 1):
    print(f'{i} {current}')
    current += (current * p) / 100
