class Person:
    name = "Vasya"


id_1 = Person()
id_1.name = "Lena"
Person.name = "Masha"
print(Person.name, id_1.name, sep='\n')
