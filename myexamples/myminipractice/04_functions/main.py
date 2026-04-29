def square(n):
    return n*n

print(f"Square of 4 is {square(4)}")
print(f"Square of 7 is {square(7)}")

def shout(text):
    print(text.upper())

shout("marshaale")
shout("tood")

# Function defining is when you create the function. it exists but does not executes result.
# Function calling is when you use the function.

def introduce(first,last):
    print(first,last)

introduce(last="Ahmed",first="Muktar")

def is_even(number):
    return number % 2 == 0

print(is_even(100))
print(is_even(7))

def max_of_two(a,b):
    if a > b:
        return a
    if b > a:
        return b
    return

print(max_of_two(10,10))
print(max_of_two(10,11))
print(max_of_two(100,10))

def stats(a,b):
    return a+b,b*a

a,b = stats(10,22)

print(a)
print(b)

def divider(a,b=2):
    return a / b

print(divider(10))

def data(x,items=None):
    if not items:
        items = [1,2,3,4]
    return x,items

print(data(22))
print(data(33,[1,7]))

def first_and_rest(head,*tail):
    return f"Head {head}",f"Rest count {len(tail)}"

print(first_and_rest(3,1,2,4,5,6,7,8))
print(first_and_rest(5,2,4,7,3,8))

