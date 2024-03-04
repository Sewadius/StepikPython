class Buildings:
    def __init__(self, x, y):
        self.check_build(x, y)

    @staticmethod
    def check_build(x, y):
        if x in (1, 200, 500, 1920) or y in (1, 300, 600, 1080):
            print('Объект в этом месте невозможен')
            return
        print('Объект построен')


kitchen = Buildings(20, 800)
living_room = Buildings(400, 500)
garage = Buildings(900, 600)
forge = Buildings(1920, 280)
dining_room = Buildings(300, 500)
