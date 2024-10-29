# Без дубликатов
print(*list(dict.fromkeys([input() for _ in range(int(input()))])), sep='\n')
