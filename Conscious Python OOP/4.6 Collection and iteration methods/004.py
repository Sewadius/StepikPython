class MyList:
    def __init__(self):
        self.data = [1, 2, 3]
        self.index = 0

    def __iter__(self):
        print('Запустился __iter__')
        return self

    def __next__(self):
        print('Запустился __next__')
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item


my_list = MyList()
for _ in my_list:
    ...
