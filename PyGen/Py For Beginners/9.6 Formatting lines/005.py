# (Не) Активное похудение
DAYS, HIGH, LOW = 60, 100, 88
OK, NO = 'Все идет по плану', 'Что-то пошло не так'

day, weight = int(input()), float(input())
count_weight = HIGH - ((HIGH - LOW) / DAYS) * day

print(OK if weight <= count_weight else NO)
print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг', end=', ')
print(f'ЦЕЛЬ по ВЕСУ = {count_weight} кг')
