class Number:
    def __init__(self, number: int):
        self.number = number

    def __add__(self, other):
        if isinstance(other, Number):
            return self.number + other.number
        if isinstance(other, int):
            return self.number + other


num1, num2 = Number(100), Number(200)
print(num1 + num2, num1 + 300, num2 + 300, sep='\n')
