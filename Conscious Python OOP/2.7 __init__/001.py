class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


coord = Coordinate(100, 200)
[print(coord.__dict__.get(i), end=' ') for i in coord.__dict__]
