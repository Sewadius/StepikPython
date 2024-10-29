# Корректный ip-адрес
print(('НЕТ', 'ДА')[all(int(i) in range(0, 256) for i in input().split('.'))])
