class Number:
    def __init__(self, number: int):
        self.number = number

    def __pow__(self, power):
        if isinstance(power, int):
            return self.number ** power


print(Number(10) ** 2)
