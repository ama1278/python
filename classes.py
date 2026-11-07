class City:
    def __init__(self, province, name, area, population):
        self.province = province
        self.name = name
        self.area = area
        self.population = population

    def __str__(self):
        return f"city{self.name} provine {self.province} |area {self.area}|population: {self.population}"


class Kasr:
        def __init__(kasr,soorat,makhraj):
                if isinstance(soorat,int)==False or isinstance(makhraj,int)==False:
                        raise TypeError
                kasr.soorat=soorat
                kasr.makhraj=makhraj
                
        def gcd(kasr,soorat,makhraj):
                sooratt=[]
                makhrajj=[]
                mosh=[]
                biiggest=0
                for i in range(1,soorat+1): 
                        if soorat%i==0:
                                sooratt.append(i)
                for j in range(1,makhraj+1):
                        if makhraj%j==0:
                                makhrajj.append(j)
                for so in sooratt:
                        if so in makhrajj:
                                mosh.append(so)
                biiggest=max(mosh)                
                return biiggest                                
        def sadeh(kasr):
                gCd=kasr.gcd(kasr.soorat,kasr.makhraj)
                kasr.soorat//=gCd
                kasr.makhraj//=gCd
                return kasr
        def __str__(self):
                return f"{self.soorat}/{self.makhraj}"


class Student:
    def __init__(self, nc, name, grade):
        self.nc = nc
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"student {self.name}  national code {self.nc}  grade {self.grade}"


class Zoo:
    def __init__(self, location, numberOF_cages):
        self.location = location
        self.numberOF_cages = numberOF_cages

    def __str__(self):
        return f" zoo lacated {self.location}  number of cages {self.numberOF_cages}"


class Human:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def __str__(self):
        return f"{self.name}  age: {self.age}  gender {self.gender}"


class Animal:
    def __init__(self, name, species, sound, age):
        self.name = name
        self.species = species
        self.sound = sound
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.species})  sound {self.sound}  age {self.age}"


class game:
    def __init__(self, name, producer, genre):
        self.name = name
        self.producer = producer
        self.genre = genre

    def __str__(self):
        return f"{self.name}  produced by {self.producer} \n genre: {self.genre}"


class product:
    def __init__(self,name, price, date_of_expiration):
        self.name=name
        self.price = price
        self.date_of_expiration = date_of_expiration

    def __str__(self):
        return f"{self.name}  {self.price}  will expire in  {self.date_of_expiration}"


class movie:
    def __init__(self, name, genre, leading_actor):
        self.name = name
        self.genre = genre
        self.leading_actor = leading_actor

    def __str__(self):
        return f"movie {self.name} is a {self.genre} movie \n leading actor: {self.leading_actor}"



city1 =City("alborz", "karaj", 130, 400000)
fraction1 = Kasr(3, 4)
student1 = Student("0012345678", "amir abdollahi", "tenth")
zoo1= Zoo("eram", 25)
human1= Human(30, "amir abdollahi", "male")
animal1 = Animal("cat", "feline", "meow", 5)
game1 = game("The Witcher 3", "CD Projekt Red", "RPG")
product1 = product("chcplate cake",45000, "1405/12/01")
movie1 = movie("odyssey","action", "matt damon")

print(city1)
print(fraction1)
print(student1)
print(zoo1)
print(human1)
print(animal1)
print(game1)
print(product1)
print(movie1)