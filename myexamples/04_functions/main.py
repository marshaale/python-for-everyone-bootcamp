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

def calculate_price(price):
    discount = 0.1
    if price >= 100:
        return price - (price * discount)
    return price

print(calculate_price(100))
print(calculate_price(90))


def repeat(word,times=2):
    print(word*times)

repeat("Hi ")
repeat("hh",10)

print(*[1,2,3])

def summarize(*args):
    return sum(args)

print(summarize(1,2,3))
print(summarize(1,2,3,5,7))

def payment_details(**info):
    return info

print(payment_details(method="Evc",sender_phone="1234788",receiver_phone="12349104",amount=111,datetime="05-05-2025 14:30"))