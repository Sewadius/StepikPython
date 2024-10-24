# Накручиваем стоимость ответа
ENG, RUS = 'eyopaxcETOPAHXCBM', 'еуорахсЕТОРАНХСВМ'

def count_amount(text: str) -> int:
    return sum(ord(ch) * 3 for ch in text)

s, new_s = input(), ''

for i in s:                             # Для каждого символа
    if i in ENG:                        # Есть английская буква
        pos = ENG.find(i)               # Находим позицию
        new_s = f'{new_s}{RUS[pos]}'    # Добавляем русскую
        continue
    new_s = f'{new_s}{i}'               # Просто копируем символ

total_old, total_new = (count_amount(i) for i in (s, new_s))

print(f'Старая стоимость: {total_old}🐝')
print(f'Новая стоимость: {total_new}🐝')
