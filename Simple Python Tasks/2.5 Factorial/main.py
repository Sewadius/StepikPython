n = int(input())
print(f'Факториал числа {n} равен '
      f'{__import__("math").factorial(n)}'
      if n > -1 else 'Число меньше нуля!')
