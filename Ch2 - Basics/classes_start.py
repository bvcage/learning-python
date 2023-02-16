#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, body_style):
        self.body_style = body_style

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, engine_type):
        super().__init__("Car")   # creates Vehicle with body_style of car
        self.wheels = 4
        self.doors = 4
        self.engine_type = engine_type
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine_type, "car at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, engine_type, has_side_car):
        super().__init__("Motorcycle")  # creates Vehicle with body_style of Motorcycle
        if (has_side_car):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engine_type = engine_type

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine_type, "motorcycle at", self.speed)


car1 = Car("gas")
car2 = Car("electric")
moto1 = Motorcycle("gas", True)

print(moto1.wheels)
print(car1.engine_type)
print(car2.doors)

car1.drive(30)
car2.drive(40)
moto1.drive(50)