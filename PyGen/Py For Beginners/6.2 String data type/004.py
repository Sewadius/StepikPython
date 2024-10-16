# Три города
(lst := list(input() for _ in '123')).sort(key=lambda i: (len(i), i))
print(lst[0], lst[-1], sep='\n')
