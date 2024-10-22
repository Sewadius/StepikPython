# Первые 12 символов
from itertools import count

STOP = 10
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

for i in count():
    print(s[i], end='')
    if i > STOP:
        break
