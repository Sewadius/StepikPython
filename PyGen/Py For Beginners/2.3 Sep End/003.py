# Кастомный разделитель
s = input()
lst = [input() for _ in range(3)]
print(*lst, sep=s)
