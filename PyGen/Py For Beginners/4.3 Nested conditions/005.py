# Церемония взвешивания
W = 'Легкий', 'Первый полусредний', 'Полусредний'

n = int(input())
print(W[0] if n < 60 else W[1] if n < 64 else W[-1], 'вес')
