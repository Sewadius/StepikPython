lst = [int(i) for i in input().split()]
n = int(input())
print(f'Число {n}' + ('' if n in lst else ' не') + ' входит в список')