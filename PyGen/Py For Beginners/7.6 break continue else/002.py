# Следуй правилам
def check(n):
    b1 = n in range(5, 10)
    b2 = n in range(17, 38)
    b3 = n in range(78, 88)
    return b1 or b2 or b3

for i in range(1, int(input()) + 1):
    if check(i):
        continue
    print(i)
