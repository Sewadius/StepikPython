# Самое тяжелое слово
heavy, weight = '', 0

for _ in range(4):
    s = input()
    current = sum(ord(i) for i in s)
    if current > weight:
        weight, heavy = current, s

print(heavy)
