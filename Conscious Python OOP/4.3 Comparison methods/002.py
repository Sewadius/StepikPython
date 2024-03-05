class Lists:
    def __init__(self, lists):
        self.lists = lists

    def __lt__(self, other):
        if isinstance(other, Lists):
            return len(self.lists) < len(other.lists)


lst1 = Lists(["a", "b", "c"])
lst2 = Lists([1, 2, 3, 4, 5])
print(lst1 < lst2)  # True
print(lst1 > lst2)  # False
