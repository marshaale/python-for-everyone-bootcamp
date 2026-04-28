def greet(name):
    print("Hi",name)

greet("Hassan")


def say_good_night(name):
    print(f"Good night {name}....")

say_good_night("Jordan")

def add(a,b):
    print(f"{a} + {b} = {a+b}")

add(12,10)

def power(base,exponent):
    print(f"Power of base {base} and exponent {exponent} is {base ** exponent}")

# Positional argument
power(2,4)

# Key argument
power(exponent=4,base=2)

def item_details(name,price,in_stock):
    print(f"{name}, {in_stock} is remaining in stock and per price is ${price}")

item_details(in_stock=5,name="iphone xr",price=189)