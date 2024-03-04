class MyClass:
    @classmethod
    def my_method(cls, x: int, y: int) -> None:
        cls.x = x
        cls.y = y
        print(x * y)


MyClass.my_method(5, 20)
