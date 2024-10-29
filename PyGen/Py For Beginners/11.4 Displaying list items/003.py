# Remove outliers
n = int(input())
lst = [int(input()) for _ in range(n)]

del lst[lst.index(max(lst))]
del lst[lst.index(min(lst))]

print(*lst, sep='\n')
