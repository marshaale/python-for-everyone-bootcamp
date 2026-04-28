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