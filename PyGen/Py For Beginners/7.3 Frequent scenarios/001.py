# Количество чисел
def check(n) -> bool:
    n **= 3
    return n % 10 in (4, 9)


a, b = (int(input()) for _ in '12')
print(len([i for i in range(a, b + 1) if check(i)]))
