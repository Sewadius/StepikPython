# Автомобильный номер
LETTERS = 'АВЕКМНОРСТУХ'
s = input()

# Длина строки и проверка разделителя
if len(s) < 9 or len(s) > 10 or s[6] != '_':
    print('NO')
    exit(0)

b1 = all(s[i] in LETTERS for i in (0, 4, 5))            # Буквы
b2 = s[1:4].isdigit() and s[7:].isdigit()               # Цифры

print(('NO', 'YES')[b1 and b2])                         # Все условия
