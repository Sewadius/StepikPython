def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(__import__('math').sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
print(f'{n} является ' +
      ('простым' if is_prime(n) else 'составным') + ' числом')
