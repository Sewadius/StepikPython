# Сумма минимального и максимального
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
numbers.sort()

print(sum(numbers[i] for i in (0, -1)))
