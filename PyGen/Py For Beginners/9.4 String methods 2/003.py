# Очень странные дела
from itertools import count
counter = count()

for _ in range(int(input())):
    msg = input()
    if msg.count('11') > 2:
        next(counter)

print(next(counter))

