class StopNumber:
    def __new__(cls, number: int, name: str):
        if number < 1000:
            return
        return super().__new__(cls)

    def __init__(self, number: int, name: str):
        self.number = number
        self.name = name


Masha = StopNumber(500, 'Masha')
Vika = StopNumber(1500, 'Vika')
Lena = StopNumber(1200, 'Lena')

print(isinstance(Masha, StopNumber))
print(isinstance(Vika, StopNumber))
print(isinstance(Lena, StopNumber))
