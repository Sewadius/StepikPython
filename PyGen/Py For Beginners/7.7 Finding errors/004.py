# Ревью кода - 4
result = []

for i in input():
    if i in ('0', '3', '6', '9'):
        result.append(int(i))

print(max(result) if result else 'NO')
