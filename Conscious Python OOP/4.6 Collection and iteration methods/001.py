class MyPhone:
    def __init__(self):
        self.phone = ['Nokia', 'Iphone', 'Samsung', 'Huawei', 'LG']

    def __str__(self):
        return str(self.phone)

    def __getitem__(self, item):
        return self.phone[item]

    def __setitem__(self, key, value):
        self.phone[key] = value

    def __delitem__(self, key):
        del self.phone[key]

    def kruchu_verchu(self, value):
        self.phone.append(value)


my_phone = MyPhone()

my_phone[1] = 'Xiaomi'
del my_phone[2]
my_phone.kruchu_verchu('HONOR')

print(my_phone)
print(my_phone[4])
