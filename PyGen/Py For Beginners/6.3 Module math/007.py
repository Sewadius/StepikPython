# Правильный многоугольник
from math import pi, tan

n, a = (float(input()) for _ in '12')
print((n * a * a) / (4 * tan(pi / n)))
