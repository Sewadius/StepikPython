# Ремонт
from math import ceil

l, w, h = map(int, input().split())
surface = 2 * (w * h + l * h)
print(ceil(surface / 16))

