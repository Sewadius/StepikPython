# Гласные и согласные
TEXT = 'Количество {} букв равно'
VOWELS = 'ауоыиэяюе'
CONSONANTS = 'бвгджзйклмнпрстфхцчшщ'

s = input()
vow_count = len([i for i in s if i.lower() in VOWELS])
con_count = len([i for i in s if i.lower() in CONSONANTS])

print(TEXT.format('гласных'), vow_count)
print(TEXT.format('согласных'), con_count)
