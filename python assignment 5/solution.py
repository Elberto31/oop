# Activity 1: Class with Attributes, Methods, and Inheritance
class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level  # Battery level as a percentage
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Battery: {self.battery_level}%")
    
    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"{self.model} is charged to {self.battery_level}%.")

# Derived class - Inherits from Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_level, cooling_system):
        super().__init__(brand, model, battery_level)
        self.cooling_system = cooling_system  # Whether it has a cooling system
    
    def display_info(self):
        super().display_info()
        print(f"Cooling System: {'Enabled' if self.cooling_system else 'Disabled'}")
    
    def play_game(self, game_name):
        if self.battery_level > 10:
            print(f"Playing {game_name} on {self.model} with cooling system {'ON' if self.cooling_system else 'OFF'}!")
            self.battery_level -= 10
        else:
            print("Battery too low to play games! Please charge the phone.")

# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗.")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing 🚤.")

class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is pedaling 🚲.")

# Main function
def main():
    # Activity 1
    print("---- Smartphone Example ----")
    phone1 = Smartphone("Samsung", "Galaxy S21", 50)
    phone1.display_info()
    phone1.charge(30)

    gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 40, True)
    gaming_phone.display_info()
    gaming_phone.play_game("PUBG Mobile")
    gaming_phone.charge(20)

    # Activity 2
    print("\n---- Polymorphism Example ----")
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    for vehicle in vehicles:
        vehicle.move()  # Calls move() method depending on the class

if __name__ == "__main__":
    main()
