# Наибольшее и наименьшее
MSG = 'Наименьшее', 'Наибольшее'
n = sorted(int(input()) for _ in range(5))

for i, val in enumerate(MSG):
    print(f'{val} число =', n[0] if i == 0 else n[-1])
