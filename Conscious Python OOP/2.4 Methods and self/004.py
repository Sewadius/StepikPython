class NewJournal:
    MONEY = 80
    NOT_ENOUGH = 'Денег не хватает'
    ENOUGH = 'Ура, денег хватает!'
    ATTRIBUTES = 'papa', 'mama', 'deda', 'baba'

    def set_attr(self, *args) -> None:
        for i, arg in enumerate(args):
            setattr(self, self.ATTRIBUTES[i], arg)
        self.count_money = sum(getattr(self, i) for i in self.ATTRIBUTES)

    def check_money(self) -> None:
        check = self.count_money < self.MONEY
        print(self.NOT_ENOUGH if check else self.ENOUGH)


masha = NewJournal()
masha.set_attr(10, 20, 30, 40)
masha.check_money()
