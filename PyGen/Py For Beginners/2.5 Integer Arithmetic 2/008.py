# Перестановка цифр
n = int(input())
a, b, c = n // 100, n // 10 % 10, n % 10

print(n)
print(a * 100 + c * 10 + b)
print(b * 100 + a * 10 + c)
print(b * 100 + c * 10 + a)
print(c * 100 + a * 10 + b)
print(c * 100 + b * 10 + a)
