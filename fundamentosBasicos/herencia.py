# Base class for a car
class Car:
    def __init__(self, make, model, year):
        # Marca del auto
        self.make = make
        # Modelo del auto
        self.model = model
        # Año del auto
        self.year = year

    def display_info(self):
        # Muestra la información del auto
        print(f"{self.year} {self.make} {self.model}")

# Subclass for an electric car
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        # Llama al constructor de la clase base
        super().__init__(make, model, year)
        # Tamaño de la batería del auto eléctrico
        self.battery_size = battery_size

    def display_battery_info(self):
        # Muestra la información de la batería
        print(f"Battery size: {self.battery_size} kWh")

# Subclass for a gasoline car
class GasolineCar(Car):
    def __init__(self, make, model, year, fuel_tank_size):
        # Llama al constructor de la clase base
        super().__init__(make, model, year)
        # Tamaño del tanque de combustible del auto a gasolina
        self.fuel_tank_size = fuel_tank_size

    def display_fuel_tank_info(self):
        # Muestra la información del tanque de combustible
        print(f"Fuel tank size: {self.fuel_tank_size} liters")

# Crear instancias de autos
tesla = ElectricCar("Tesla", "Model S", 2022, 100)
toyota = GasolineCar("Toyota", "Corolla", 2021, 50)

# Mostrar información de los autos
tesla.display_info()
tesla.display_battery_info()

toyota.display_info()
toyota.display_fuel_tank_info()