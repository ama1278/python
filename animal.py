class Animal:
    def __init__(self,name,species,age):
        self.name=name
        self.species=species
        self.age=age
    def __str__(self):
        return f'name: {self.name} , species: {self.species} \nage: {self.age}'
leopard=Animal("leopard",'feline',5)
cat=Animal("cat",'scottish cat',1)
lion=Animal("lion",'african lion',3)
print(leopard)        
        