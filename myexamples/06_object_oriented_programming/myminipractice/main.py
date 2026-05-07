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

