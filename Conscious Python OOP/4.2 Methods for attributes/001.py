class User:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        return f'{object.__getattribute__(self, item)}man'


user1 = User("Super")
user2 = User("Bat")
user3 = User("Spider")

print(user1.name, user2.name, user3.name, sep='\n')
