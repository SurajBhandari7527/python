class Legocar:
    def __init__(self,color,speed):
        self.color=color
        self.speed=speed
    def drive(self):
        print("The {} car has speed of {}".format(self.color,self.speed))
red_car=Legocar('red',15)
red_car.drive()
blue_car=Legocar('blue',20)
blue_car.drive()

