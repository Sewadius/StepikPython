# Ведьмаку заплатите чеканной монетой
from itertools import count

COINS = [25, 10, 5, 1]
counter = count()

n = int(input())

for i in range(len(COINS)):
    while n >= COINS[i]:
        next(counter)
        n -= COINS[i]

print(next(counter))
