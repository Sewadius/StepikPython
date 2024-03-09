l1, l2 = [list(map(int, input().split())) for _ in range(2)]
print(f'Списки ' + ('' if l1 == l2 else 'не ') + 'совпадают')
