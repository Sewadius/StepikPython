# Парты
from math import ceil

a, b, c = (int(input()) for _ in '123')
a = ceil(a / 2)
b = ceil(b / 2)
c = ceil(c / 2)
print(a + b + c)
