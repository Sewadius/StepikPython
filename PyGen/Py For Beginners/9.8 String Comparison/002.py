# Волшебное число
lst = [input() for _ in '1234']
result = ord(min(lst)[-1]) * ord(max(lst)[-1])
print(result ** 2)
