# Электронные часы 2
n = int(input())
n = n % (60 * 60 * 24)

h = n // (60 * 60)
m = n // 60 % 60
s = n % 60

print(h, end=':')
print(m // 10, m % 10, sep='', end=':')
print(s // 10, s % 10, sep='')
