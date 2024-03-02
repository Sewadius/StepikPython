class Coordinate:
    ...


coord = Coordinate()
coord.__setattr__('x', 100)
coord.x = 5
print(coord.x)
