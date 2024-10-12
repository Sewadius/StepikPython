# Наименьшее из двух чисел
a, b = (int(input()) for _ in range(2))
print(a if a < b else b)
