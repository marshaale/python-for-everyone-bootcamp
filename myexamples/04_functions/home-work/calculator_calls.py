def multiply(a,b):
    return a*b

print("Result:",multiply(2,4)) # Position arg order is necessary.
print("Result:",multiply(a=3,b=3))
print("Result:",multiply(b=5,a=2)) # Keyword arg position is mandatory.
