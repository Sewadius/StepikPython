# Стоимость ответа
s = input()
amount = sum(ord(i) * 3 for i in s)

print(f"Текст сообщения: '{s}'")
print(f'Стоимость сообщения: {amount}🐝')

