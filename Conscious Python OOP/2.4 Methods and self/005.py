class GPS:
    distance1 = ("Москва", "Екатеринбург", 1860)
    distance2 = ("Москва", "Казань", 840)
    distance3 = ("Москва", "Нижний Новгород", 430)

    def count_distance(self, point1: str, point2: str) -> None:
        if point1 == point2:
            print(0)
            return

        for distance in self.distance1, self.distance2, self.distance3:
            if point1 in distance and point2 in distance:
                print(distance[-1])
                break
        else:
            print('Извините, программа ещё в разработке')


dis1 = GPS()
dis2 = GPS()
dis3 = GPS()

dis1.count_distance("Москва", "Казань")
dis2.count_distance("Екатеринбург", "Москва")
dis2.count_distance("Казань", "Казань")
dis3.count_distance("Нижний Новгород", "Екатеринбург")
