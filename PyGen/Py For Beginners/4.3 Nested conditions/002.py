# Вид треугольника
TYPE = 'Равносторонний', 'Равнобедренный', 'Разносторонний'

a, b, c = (int(input()) for _ in range(3))
equilateral = a == b == c
isosceles = a == b or a == c or b == c

print(TYPE[0] if equilateral else TYPE[1] if isosceles else TYPE[-1])
