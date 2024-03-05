class King:
    a = 4


class Queen:
    b = 6


class Prince(King, Queen):
    c = 10


count = Prince()
print(sum([count.a, count.b, count.c]))
