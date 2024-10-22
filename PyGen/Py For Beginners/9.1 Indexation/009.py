# Одинаковые соседи
from itertools import count

s = input()
counter = count()

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        next(counter)

print(next(counter))
