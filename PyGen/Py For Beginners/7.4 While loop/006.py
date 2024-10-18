# Количество пятёрок
from sys import stdin
from itertools import count

counter = count()

for i in stdin.read().split('\n'):
    if int(i).__eq__(5):
        next(counter)

    if int(i) <= 0 or int(i) > 5:
        break

print(next(counter))
