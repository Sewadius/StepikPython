# Самописный калькулятор
a, b, operation = (input() for _ in range(3))

if b == '0' and operation == '/':
    print('На ноль делить нельзя!')
    exit(0)

if operation not in ('+', '-', '*', '/'):
    print('Неверная операция')
    exit(0)

print(eval(a + operation + b))
