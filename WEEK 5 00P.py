# Name: [Your Name]
# Course: [Course Name]
# Assignment 1 & Activity 2
# Date: [Date]

# -------------------------------------------------------
# Assignment 1: Design Your Own Class 🏗️
# Superhero Example with Inheritance

class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength
    
    def show_details(self):
        print(f"Hero: {self.name}, Power: {self.power}, Strength: {self.strength}")
    
    def train(self):
        """Increase strength after training"""
        self.strength += 10
        print(f"{self.name} trained hard! Strength is now {self.strength}.")


# Inherited Class
class FlyingHero(Superhero):
    def __init__(self, name, power, strength, flight_speed):
        super().__init__(name, power, strength)
        self.flight_speed = flight_speed
    
    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")


class StrongHero(Superhero):
    def __init__(self, name, power, strength, lifting_power):
        super().__init__(name, power, strength)
        self.lifting_power = lifting_power
    
    def lift(self):
        print(f"{self.name} lifted {self.lifting_power} tons easily!")


# Example usage
hero1 = FlyingHero("SkyMan", "Control of wind", 70, 500)
hero2 = StrongHero("RockGirl", "Super strength", 90, 200)

hero1.show_details()
hero1.fly()
hero1.train()

hero2.show_details()
hero2.lift()
hero2.train()


# -------------------------------------------------------
# Activity 2: Polymorphism Challenge 🎭

class Vehicle:
    def move(self):
        pass  # placeholder for child classes


class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")


class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")


class Boat(Vehicle):
    def move(self):
        print("🚤 The boat is sailing on the water.")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

print("\n--- Vehicle Movements ---")
for v in vehicles:
    v.move()
