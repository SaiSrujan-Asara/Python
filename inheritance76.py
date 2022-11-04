class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


# inherit from vehicle class
class Car(Vehicle):
    def __init__(self, name, color, price, siz):
        self.siz = siz
        Vehicle.__init__(self, name, color, price)
    
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')
    
    def size(self):
        print(f"Size of the car is {self.siz}")


# Car Object
car = Car('Car x1', 'Red', 20000, "suv")
car.size()


a = Vehicle("scooty","blue",2000)
a.show()
print("---------------------------------")
