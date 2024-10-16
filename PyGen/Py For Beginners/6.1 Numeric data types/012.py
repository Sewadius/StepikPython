# Манхэттенское расстояние
p1, p2, q1, q2 = (int(input()) for _ in range(4))
print(sum([abs(i) for i in (p1 - q1, p2 - q2)]))
