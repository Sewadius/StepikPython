# Асимптотическое приближение
from math import log

n = int(input())
print(sum(1 / i for i in range(1, n + 1)) - log(n))
