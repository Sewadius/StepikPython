# Необычное сравнение
s1, s2 = input(), input()

def make_string(s: str) -> str:
    res = ''

    for ch in s:
        if ch.isalpha():
            res = f'{res}{ch.lower()}'

    return res

print(('NO', 'YES')[make_string(s1) == make_string(s2)])
