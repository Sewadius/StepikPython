# Выражение
a, b, c = (int(input()) for _ in '123')

r1 = a + b * c
r2 = a * (b + c)
r3 = a * b * c
r4 = (a + b) * c
r5 = a + b + c

print(max(r1, r2, r3, r4, r5))
