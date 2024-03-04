class Counter:
    count = 0

    @classmethod
    def add_count(cls, add: int = 1) -> None:
        cls.count += add

    @classmethod
    def set_zero(cls) -> None:
        cls.count = 0


Counter.add_count()
Counter.set_zero()
Counter.add_count(110)
Counter.add_count()
print(Counter.count)
