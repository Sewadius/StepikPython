# Красивое число
n = int(input())
check_1 = 10 ** 3 <= n < 10 ** 4
check_2 = not n % 7 or not n % 17

print(('NO', 'YES')[check_1 and check_2])
