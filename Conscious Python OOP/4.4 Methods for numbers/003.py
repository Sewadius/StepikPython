class Hello:
    def __init__(self, say):
        self.say = say

    def __mul__(self, other):
        if isinstance(other, int):
            return self.say * other


lang = Hello('Hello!')
print(lang * 3)
