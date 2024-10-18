# Упорядоченные цифры
numbers = [int(i) for i in input()]
print(('NO', 'YES')[numbers == sorted(numbers, reverse=True)])
