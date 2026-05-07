class Counter:
    def __init__(self,start=0):
        self.count = start

    def bump(self):
        self.count += 1

counter = Counter(4)
counter.bump()
print(counter.count)

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

dog = Dog("John",2)
print(dog.name)
print(dog.age)

class Rectangle:
    def __init__(this,width,height):
        this.height = height
        this.width = width
    
    def area(this):
        return this.width * this.height
    
    def perimeter(this):
        return 2 * (this.width + this.height)

r1 = Rectangle(5,5)
print(r1.area())
r2 = Rectangle(25,5)
print(r2.area())
print(r2.perimeter())

class Ticket:
    next_id = 1
    def __init__(self,event):
        self.event = event
        self.id = self.next_id
        Ticket.next_id +=1

ticket1 = Ticket("PyCon")
ticket2 = Ticket("Meetup")
print(ticket1.id,ticket1.event)
print(ticket2.id,ticket2.event)

class Payment:
    base_discount_rate = 0.1
    def __init__(self,price):
        self.price = price
        self.amount_to_pay = price
    def calculate(self):
        if(self.price >= 100):
            self.amount_to_pay = self.price - (self.price * self.base_discount_rate)
    def pay(self):
        self.calculate()
        print(f"You have to pay {self.amount_to_pay}")

payment1 = Payment(99)
payment1.pay()
payment2 = Payment(100)
payment2.pay()

class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"Point({self.a},{self.b})"

    def __repr__(self):
        return f"{self.a!r},{self.b!r}"

point = Point(67,99)
print(point)
print(repr(point))