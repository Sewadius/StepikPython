class Present:
    def __init__(self):
        self.present = ['book', 'Iphone', 'TV', 'snowman', 'car']

    def __len__(self):
        return len(self.present) - 1

    def __getitem__(self, item):
        return self.present[item]


holiday = Present()

if len(holiday) == 4:
    print(holiday[3])
