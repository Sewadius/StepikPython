# Сумма разрядов числа
n = int(input())
a1 = n // 100
a2 = n // 10 % 10
a3 = n % 10
s = a1 + a2 + a3
print(s)
