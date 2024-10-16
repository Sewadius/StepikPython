# Средние значения
K = .5
a, b = (float(input()) for _ in '12')

print((a + b) * K)
print((a * b) ** K)
print(K ** -1 * a * b / (a + b))
print(((a * a + b * b) * K) ** K)
