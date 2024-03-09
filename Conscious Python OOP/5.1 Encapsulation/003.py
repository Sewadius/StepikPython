class MagicBank:
    def __init__(self, account, balance):
        self.__account = account
        self.__balance = balance

    @property
    def happy_balance(self):
        return self.__balance

    @happy_balance.setter
    def happy_balance(self, value):
        self.__balance = value

    @happy_balance.deleter
    def happy_balance(self):
        self.__balance = 0


id_1 = MagicBank('Машенька', 500)
print(id_1.happy_balance)

id_1.happy_balance = 1000
print(id_1.happy_balance)

del id_1.happy_balance
print(id_1.happy_balance)
