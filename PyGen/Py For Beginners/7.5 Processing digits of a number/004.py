# Все вместе
from numpy import prod, mean

lst = [int(i) for i in input()]

print(sum(lst), len(lst), sep='\n')
print(prod(lst), mean(lst), sep='\n')
print(lst[0], lst[0] + lst[-1], sep='\n')
