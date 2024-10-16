# Евклидово расстояние
x1, y1, x2, y2 = (float(input()) for _ in '1234')
print(__import__('math').hypot(x1 - x2, y1 - y2))
