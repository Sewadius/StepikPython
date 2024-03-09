class Bank:
    def __init__(self, name: str, card: int, balance: int):
        self.__name = name
        self.__card = card
        self.__balance = balance

    def print_balance(self) -> None:
        print(f'{self.__balance}')

    def change_balance(self, money: int):
        self.__balance += money


id_1 = Bank('Vasya', 12345678, 500)
id_1.change_balance(-500)
id_1.print_balance()
