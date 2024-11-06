# Две половинки
s = input()
edge = (len(s) + 1) // 2
print(f'{s[edge:]}{s[:edge]}')
