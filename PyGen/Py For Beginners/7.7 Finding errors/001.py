# Ревью кода - 1
from numpy import prod

lst = [n for _ in range(10) if (n := int(input())) >= 0]

if not lst:
    print('NO')
    exit(0)

print(len(lst), prod(lst), sep='\n')
