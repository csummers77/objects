class Car(object):
    def __init__(self,make,model,mpg):
        self.make = make
        self.model = model
        self.mpg = mpg
    def startCar(self):
        print "%s goes Vroom" % self.make
myCar = Car('ford','focus', 40)
myCar.startCar()

class ElectricCar(Car):
    # call this object constructor
    def __init__(self,make,model,batteryLife):
        super(ElectricCar,self).__init__(make,model,"N/A")
        self.batteryLife = batteryLife
    def startCar(self):
             print "%s goes..." % self.make
car1 = Car("Toyota","Camary",35)
car2 = ElectricCar("Tesla","S","100kh")
print car1.model
print car2.mpg
car2.startCar()