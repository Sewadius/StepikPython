# Количество совпадающих пар
from itertools import count

counter = count()
lst = [int(i) for i in input().split()]

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            next(counter)

print(next(counter))
