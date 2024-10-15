# Ход ладьи
a1, b1, a2, b2 = (int(input()) for _ in range(4))
print(('NO', 'YES')[a1 == a2 or b1 == b2])
