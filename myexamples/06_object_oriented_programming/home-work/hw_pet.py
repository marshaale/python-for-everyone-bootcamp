class Pet:
    def __init__(self,name,species):
        self.name = name
        self.species = species

dog = Pet("jane","detective dog")
cat = Pet("kit","familiar")

print(dog.name)
print(cat.name)