# Пересечение отрезков
a1, b1, a2, b2 = (int(input()) for _ in range(4))

# Пустое множество
if b1 < a2 or b2 < a1:
    print('пустое множество')
    exit(0)

# Точка
if b1 == a2 or b2 == a1:
    print(b1 if b1 == a2 else b2)
    exit(0)

# Второй внутри первого
if a2 >= a1 and b2 <= b1:
    print(a2, b2)
    exit(0)

# Первый внутри второго
if a1 >= a2 and b1 <= b2:
    print(a1, b1)
    exit(0)

# Пересечение
if a2 < b1 < b2:
    print(a2, b1)
elif a2 < a1 < b2:
    print(a1, b2)
