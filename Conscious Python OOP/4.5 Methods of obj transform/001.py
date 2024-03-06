class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Да здравствует {self.name}!'


input_word = input()
person = Person(input_word)
print(person)
