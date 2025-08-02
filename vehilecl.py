class BMW:
    def __init__(self,max_speed,Fuel):
        self.max_speed=max_speed
        self.Fuel=Fuel


    def car(self):
        print("The max car speed is",self.max_speed)
        print("The amount of fuel in the car is",self.Fuel)

class Ferrari:
    def __init__(self,max_speed,Fuel):
        self.max_speed=max_speed
        self.Fuel=Fuel


    def car(self):
        print("The max car speed is",self.max_speed)
        print("The amount of fuel in the car is",self.Fuel)


ferar=Ferrari(200,120)
bwm=BMW(175,200)

for stats in (ferar,bwm):
    stats.car()