class Car:
    def __init__(self,brand):
        self.brand = brand
        print("Car is created")

car = Car("Toyota")
print(car.brand)

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book({self.title!r},{self.author!r},{self.pages!r})"


book1 = Book("The way out","Gerard",210)
book2 = Book("How to say no!","Denis",150)
print(book1)
print(book1.title,book1.pages)
print(book2.title,book2.pages)
print(book2)

print("Repr",repr(book1))
print("Repr",repr(book2))

# Book class is the blueprint or template no book exists.
# b = Book() is the instance of the blueprint or the template actual book exists.

class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount

account = BankAccount()
account.deposit(10)
account.deposit(5)
print(account.balance)


class Dog:
    species = "Detective dog"
    def __init__(self,name):
        self.name = name

jane = Dog("Jane")
reckon = Dog("Reckon")
print(jane.species,reckon.species)

class Counter:
    total_created = 0
    def __init__(self):
        Counter.total_created +=1

c1 = Counter()
c2 = Counter()
print(Counter.total_created)

class School:
    teachers = [] # This means teachers is shared across all instances
    def __init__(self,name):
        self.name = name

school = School("cali hussein")
school.teachers.append("Jane Doe")
print(school.teachers)
school2 = School("al masal")
school2.teachers.append("John Doe")
print(school2.teachers)

class SafeSchool:
    def __init__(self,name,teachers):
        self.name = name
        self.teachers = teachers # This means teachers is dedicated by instances

school3 = SafeSchool("badbaado",['ali','kali'])
print(school3.teachers)
school4 = SafeSchool("mogadishu",['abdi','maria'])
print(school4.teachers)

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
        self.side = side
    
    def __str__(self):
        return f"Square(side={self.side})"

square = Square(5) # 25
print(square)
print(square.area())

from dataclasses import dataclass

@dataclass
class Paper:
    title:str
    author:str
    pages:int = 0

    def short_title(self):
        return self.title[:10]

paper = Paper("The long way out","John Doe")
paper2 = Paper("The long way out","John Doe")
print(paper.short_title())
print(paper)

print(paper == paper2)

@dataclass
class Player:
    name:str

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self,player_name):
        self.players.append(Player(player_name))
    
    def roaster(self):
        for player in self.players:
            print(player.name)
    
    def __str__(self):
        return f"Team(name={self.name},players={self.players})"

team = Team("Team A")
team.add_player("Hakimi")
team.add_player("Ronaldo")
team.add_player("Messi")
team.roaster()
print(team)

# Players is members of the team not is a team. So we use composition not inheritance.

class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} speaking...........")

# a Lion is an animal not has an animal so we use inheritance
class Lion(Animal):
    def walk(self):
        print(f"{self.name} walking............")

# an arena has animals not is an animal so we use composition
class Arena:
    def __init__(self,name):
        self.name = name
        self.animals = []
    
    def add_animal(self,animal):
        self.animals.append(animal)
    
    def show_animals(self):
        for animal in self.animals:
            print(animal.name)

arena = Arena("Arena-1")
arena.add_animal(Lion("Simba"))
arena.add_animal(Lion("Nala"))
arena.show_animals()

# Library is not inherit book because a library has many books. if library inherit a book it means library is a book.