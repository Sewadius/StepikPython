class Number:
    def __init__(self, number: int):
        self.number = number

    def __add__(self, other):
        if isinstance(other, int):
            return self.number + other

    def __sub__(self, other):
        if isinstance(other, int):
            return self.number - other

    def __mul__(self, other):
        if isinstance(other, int):
            return self.number * other

    def __truediv__(self, other):
        if isinstance(other, int) and other != 0:
            return self.number / other

    def __pow__(self, power):
        if isinstance(power, int):
            return self.number ** power

    def __abs__(self):
        return abs(self.number)


num1 = Number(-10)
result1 = num1 + 90
result2 = num1 / 10
result3 = num1 * -1
result4 = num1 ** 2
result5 = num1 - 20
result6 = abs(num1)
print(result1, result2, result3, result4, result5, result6)
