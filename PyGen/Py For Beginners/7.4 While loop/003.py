# Количество членов
from itertools import count

counter = count()
while input() not in ('стоп', 'хватит', 'достаточно'):
    next(counter)

print(next(counter))
