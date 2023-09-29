class Car:
    def __init__(self, make, model, year, engine) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        self.engine = engine
        print('Created new car')

    def accelerate(self):
        self.speed = self.engine * 100
    def brake(self):
        self.speed -= 10

myCar1 = Car("TOYOTA", "Camry", 2023, 1.5)
myCar2 = Car("HONDA", "Civic Type R", 1992, 1.3)

myCar2.accelerate()
myCar2.accelerate()
print(myCar1.speed)
print(myCar2.speed)
myCar2.brake()
print(myCar2.speed)


