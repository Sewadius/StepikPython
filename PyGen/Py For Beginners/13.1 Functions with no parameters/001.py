# Звездный прямоугольник 1
def draw_box():
    print('*' * 10)
    for _ in range(12):
        print('*', end='')
        [print(' ', end='') for _ in range(8)]
        print('*')
    print('*' * 10)

draw_box()
