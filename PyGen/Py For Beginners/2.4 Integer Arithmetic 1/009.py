# Разделяй и властвуй
x = int(input())
print(*(x * i for i in range(1, 6)), sep='---')
