# Последовательность чисел 4
def check(n):
    return not n % 17 or n % 10 == 9 or not n % 15


m1, n1 = (int(input()) for _ in '12')
[print(i) for i in range(m1, n1 + 1) if check(i)]
