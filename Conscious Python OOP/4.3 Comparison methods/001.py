class Number:
    def __init__(self, x, y):
        self.summa = x + y

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.summa == other.summa
        if isinstance(other, int):
            return self.summa == other


number_1 = Number(4, 2)
number_2 = Number(5, 5)
print(number_1 == number_2)
print(number_1 == 10)
print(number_2 == 10)
