# Название класса
lst = [input() for _ in range(int(input()))]
flag = True

for el in lst:
    if len(el) != 2:
        flag = False
    if not el[0].isdigit():
        flag = False
    if el[-1] < 'А' or el[-1] > 'П' or el[-1] == 'Ё':
        flag = False

    print(('NO', 'YES')[flag])
    flag = True
