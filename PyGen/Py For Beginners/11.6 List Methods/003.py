# Количество артиклей
FOUND = 'a', 'an', 'the'

text = list(word.lower() for word in input().split())
total = sum(el in FOUND for el in text)

print(f'Общее количество артиклей: {total}')
