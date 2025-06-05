# Прямоугольный треугольник
a, b, c = map(int, input().split())

n1 = a ** 2 == b ** 2 + c ** 2
n2 = b ** 2 == a ** 2 + c ** 2
n3 = c ** 2 == a ** 2 + b ** 2

print(n1 or n2 or n3)
