# Какая следующая буква?
letter = chr(ord(input()) + 1)
print(letter if letter.isupper() else 'Дальше букв нет')
