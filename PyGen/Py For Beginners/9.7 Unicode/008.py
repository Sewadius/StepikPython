# Сбой в системе
s = input()
FOUND = '[u-'

while s.find(FOUND) != -1:
    pos = s.find(FOUND)
    sym = s[pos + 3: pos + 7]
    s = s.replace(FOUND + sym + ']', chr(int(sym)), 1)

print(s)
