# Каждые 7 символов строки
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

for i in range(0, len(s), 7):
    print(s[i], end='')
