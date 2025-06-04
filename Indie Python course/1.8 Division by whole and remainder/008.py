# Выиграть в лотерею
n, total = int(input()), 0

total = total + n // 100
n = n % 100

total = total + n // 20
n = n % 20

total = total + n // 10
n = n % 10

total = total + n // 5
n = n % 5

print(total + n)
