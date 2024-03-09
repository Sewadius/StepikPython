l = [int(i) for i in input().split()]
print('Список ' + ('' if l == l[::-1] else 'не ') +
      'является симметричным')
