# Значение функции
numbers = list()

for _ in range(int(input())):
    numbers.append(int(input()))

print(*numbers, sep='\n')
print()

[print((i + 1) ** 2) for i in numbers]
