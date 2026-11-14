class Car:
    def __init__(self,model,price,year,owner,speed):
        self.model=model
        self.price=price
        self.age=year
        self.owner=owner
        self.speed=speed
    def start(self):
        return f"{self.model} has been started"
    def stop(self):
        self.speed=0
        return f"{self.model} has been turned off"
    def accelerate(self):
        self.speed+=10
        return self.speed
    def brake(self,time):
        for i in range(time):
            self.speed-=10
        return self.speed        
    def __str__(self):    
        return f'the {self.model} car which made in {self.age} and value about {self.price}\nowner:{self.owner}' 

car1=Car("bmw",100000,2023,"someone",100 )
print(car1)