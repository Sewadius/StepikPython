# Задание 6
storage1, storage2 = 10, 20
moving1, moving2, moving3 = 2, 3, 4

storage2 += moving1
storage1 -= moving1

storage1 += moving2
storage2 -= moving2

storage2 += moving3
storage1 -= moving3

print(storage1, storage2)
