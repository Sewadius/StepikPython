class Number:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.s = a + b
        del self.s

    def __delattr__(self, item):
        if getattr(self, item) > 10:
            return
        super().__delattr__(item)


number1 = Number(4, 5)
print('s' in number1.__dict__)

number2 = Number(6, 11)
print('s' in number2.__dict__)
