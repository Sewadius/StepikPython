# Ревью кода - 2
l = sorted(n for _ in range(10) if (n := int(input())) < 0)

if not l:
    print('NO')
    exit(0)

print(sum(l), l[-1], sep='\n')
