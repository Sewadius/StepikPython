# Первое и последнее вхождение
s = input()
counter = s.count('f')

if counter > 1:
    print(s.find('f'), s.rfind('f'))
    exit(0)

print(s.find('f') if counter else 'NO')
