# Без нулей
from numpy import prod

print(prod([int(input()) or 1 for _ in range(10)]))
