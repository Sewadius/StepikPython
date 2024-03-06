class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __hash__(self):
        return hash((self.model, self.color))


car1 = Car("toyota corolla", "black")
car2 = Car("toyota corolla", "black")
print(hash(car1) == hash(car2))
