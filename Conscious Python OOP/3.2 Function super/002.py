class Alfa:
    @staticmethod
    def sum_numbers(x: int, y: int) -> int:
        return x + y


class Beta(Alfa):
    def result(self, x: int, y: int, z: int) -> None:
        summa = super().sum_numbers(x, y)
        print(summa / z)


test = Beta()
test.result(10, 20, 30)
