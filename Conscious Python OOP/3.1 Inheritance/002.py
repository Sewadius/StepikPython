class CountDistance:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def dist_count(start, finish) -> None:
        dist = ((finish.x - start.x) ** 2 + (finish.y - finish.x) ** 2) ** .5
        print(round(dist))


class Point(CountDistance):
    pass


p1 = Point(10, 20)
p2 = Point(20, 30)
CountDistance.dist_count(p1, p2)
