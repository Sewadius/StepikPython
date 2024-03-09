from math import gcd
a, b = (int(input()) for _ in range(2))
print(f'НОК: {(a * b) // gcd(a, b)}\nНОД: {gcd(a, b)}')
