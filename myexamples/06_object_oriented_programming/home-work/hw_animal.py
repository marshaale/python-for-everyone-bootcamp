class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def __init__(self,name,bread):
        super().__init__(name)
        self.bread = bread

dog = Dog("john","breading....")
print(dog.name,dog.bread)