# Интересное число
n = int(input())
lst = sorted([n // 100, n // 10 % 10, n % 10])
check = lst[-1] - lst[0] == lst[1]

print('Число ', '' if check else 'не', 'интересное', sep='')
