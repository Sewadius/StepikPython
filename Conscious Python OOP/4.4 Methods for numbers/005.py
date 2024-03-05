class Number:
    def __init__(self, number: int):
        self.number = number

    def __truediv__(self, other):
        return 'на ноль делить нельзя' if other == 0 else self.number / other

    
num = Number(10)
print(num / 2, num / 0, sep='\n')
