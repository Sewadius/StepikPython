# Арифметические строки
s = sorted((len(input()) for _ in '123'))
print(('NO', 'YES')[s[1] - s[0] == s[-1] - s[1]])
