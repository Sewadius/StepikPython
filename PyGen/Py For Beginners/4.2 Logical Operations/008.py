# Ход короля
a1, b1, a2, b2 = (int(input()) for _ in range(4))
check = abs(a1 - a2) < 2 and abs(b1 - b2) < 2
print(('NO', 'YES')[check])
