# Вторая цифра
n = int(input())
result = n % 10

while n > 100:
    n //= 10
    result = n % 10

print(result)
