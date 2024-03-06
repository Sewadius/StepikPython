class Car:
    def __init__(self):
        self.model = 'toyota corolla'
        self.color = 'black'
        self.year = 2023

    def __repr__(self):
        return f'Класс: {self.__class__.__name__}, Атрибуты экземпляра: {self.__dict__}'


car = Car()
print(repr(car))
