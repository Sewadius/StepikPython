class Number:
    def __init__(self, number: int):
        self.number = number

    def __sub__(self, other):
        if isinstance(other, Number):
            return self.number - other.number


num1, num2 = Number(70), Number(20)
print(num1 - num2)
