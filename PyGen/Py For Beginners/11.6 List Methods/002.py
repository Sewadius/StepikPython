# Переставить min и max
lst = list(int(i) for i in input().split())

mx, mi = lst.index(max(lst)), lst.index(min(lst))
lst[mx], lst[mi] = lst[mi], lst[mx]

print(*lst)
