class Time:
    @staticmethod
    def count_time(distance: int, speed: int) -> float:
        return distance / speed


print(Time.count_time(500, 100))
