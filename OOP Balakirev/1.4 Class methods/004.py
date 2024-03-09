import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data: list) -> None:
        for line in data:
            line = line.split()
            new_data = {}
            for i, el in enumerate(DataBase.FIELDS):
                new_data[el] = line[i]
            DataBase.lst_data.append(new_data)

    def select(self, a: int, b: int) -> list:
        return DataBase.lst_data[a:b + 1]


db = DataBase()
db.insert(lst_in)
