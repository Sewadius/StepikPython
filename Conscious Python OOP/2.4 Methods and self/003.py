class Person:
    message_counter = 0

    def print_number_of_messages(self):
        print(self.message_counter)


id_1 = Person()
id_2 = Person()

id_1.message_counter = 5
id_2.message_counter = 10

[el.print_number_of_messages() for el in (id_1, id_2)]
