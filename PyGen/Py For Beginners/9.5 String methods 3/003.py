# Проверь никнейм
nick = input()

b1 = nick[0] == '@'             # Первый символ '@'
b2 = 4 < len(nick) < 16         # Длина
b3 = nick == nick.lower()       # Нижний регистр
b4 = nick[1:].isalnum()         # Только буквы и цифры

print(('Incorrect', 'Correct')[all((b1, b2, b3, b4))])
