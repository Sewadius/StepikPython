class Simpsons:
    name = 'Simpsons'

    def say_hello(self):
        print('Привет,', self.name)


bart = Simpsons()
lisa = Simpsons()
homer = Simpsons()

bart.name = 'Bart'
lisa.name = 'Lisa'
homer.name = 'Homer'

[el.say_hello() for el in (bart, lisa, homer)]
