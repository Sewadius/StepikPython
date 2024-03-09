class BeautyTransform:
    def __init__(self, height: int, weight):
        self.height = height
        self.weight = weight
        self.result = 'Божественная красота'

    def transformer(self):
        try:
            setattr(self, 'new_body', self.height / self.weight)
        except Exception:
            self.result = 'Индюк на три дня'
        else:
            print('Проверка прошла! ', end='')
        finally:
            print(f'Результат: {self.result}')


nastya = BeautyTransform(100, 50)
lena = BeautyTransform(50, 90)
vasya = BeautyTransform(172, "Индюк")

nastya.transformer()
lena.transformer()
vasya.transformer()
