class Driver:
    @staticmethod
    def calculate_fuel_costs(distance: int, fuel: int, price: int) -> None:
        print(round(price * (fuel / 100) * distance, 2))


vasya = Driver()
vasya.calculate_fuel_costs(3, 7, 50)
vasya.calculate_fuel_costs(100, 7, 50)
vasya.calculate_fuel_costs(50, 7, 50)
