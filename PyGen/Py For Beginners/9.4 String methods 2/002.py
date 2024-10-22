# Минутка генетики
s = input()
code = 'Аденин:', 'Гуанин:', 'Цитозин:', 'Тимин:'

for c in code:
    print(c, s.lower().count(c[0].lower()))

