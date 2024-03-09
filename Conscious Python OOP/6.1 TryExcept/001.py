class BeautyTransform:
    def __init__(self, height: int, weight: int = 0):
        self.height = height
        self.weight = weight

    def transformer(self):
        try:
            self.new_body = self.height / self.weight
            print('Успешная трансформация')
        except ZeroDivisionError:
            print('Лицо как в картине Крик, Эдварда Мунка')


vasya = BeautyTransform(172, 70)
nastya = BeautyTransform(100, 50)
lena = BeautyTransform(50)

vasya.transformer()
nastya.transformer()
lena.transformer()
