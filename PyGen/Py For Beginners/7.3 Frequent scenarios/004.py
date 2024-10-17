# Сумма чисел 2
print(sum(i for i in range(1, int(input()) + 1) if i * i % 10 in (2, 5, 8)))
