# Знакочередующаяся сумма
n = int(input())
print(sum((-1) ** (i + 1) * i for i in range(1, n + 1)))
