# Обратный порядок 2
a, b, size = int(input()), 0, 0
n = a

while a:
    a //= 10
    size += 1

while size:
    b += n % 10 * 10 ** (size - 1)
    n //= 10
    size -= 1

print(b)
