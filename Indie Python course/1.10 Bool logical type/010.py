# Проверка треугольника
a, b, c = map(int, input().split())

check1 = a + b > c
check2 = a + c > b
check3 = b + c > a

print(check1 and check2 and check3)
