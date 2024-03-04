class MagicBank:
    money = 1000

    @classmethod
    def add_money(cls) -> None:
        cls.money = 1000
        print('Ваш счёт снова равен 1000', end='\n\n')

    @classmethod
    def reduce_money(cls, amount: int) -> None:
        if amount > 1000:
            print('Нельзя тратить больше 1000 за один раз')
            return
        print(f'Покупка на сумму {amount} осуществлена')
        cls.add_money()


masha = MagicBank()
masha.reduce_money(100)
masha.reduce_money(999)
masha.reduce_money(1000000000)
