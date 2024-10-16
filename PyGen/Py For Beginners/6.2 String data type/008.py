# Корректный email
mail = input()
print(('NO', 'YES')[all(i in mail for i in ('@', '.'))])
