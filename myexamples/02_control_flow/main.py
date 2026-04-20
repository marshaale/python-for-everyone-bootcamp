print("Hello,"+"world")
print("Hi salma "*3)


area = 10
width = 5

print("Area + Width",area+width)
print("Area - Width",area-width)
print("Area / Width",area/width) # Division result of float.
print("Area // Width",area // width) # Division result of integer.
print("Area * Width",area*width)
print("Area ^ Width",area ** width)

people = 9
shared_amount = 100
remainder = shared_amount % people

print("Remainder of",shared_amount,"out of",people,"People is",remainder)


counter = 0
counter = counter + 10
print("First addition:",counter)

counter -= 10

print("Subtracted by 10 using assignment operator:",counter)

counter += 7

print("Second addition using assignment operator:",counter)

counter *= 3

print("Multiplied by 3 using assignment operator:",counter)

counter //= 3

print("Divission",counter)

price = 100

print(3 <= price <= 10)

print("Is area is less than width:",area < width)

print("Is area is greater than width:",area > width)

print("Is price available for discount", 50 <= price <= 250)

print(price * 0.1,price * 0.1 != 10)

print("A" == "a")

quantity = 3

print("Is discountable",price > 50 and quantity >= 5)

nira = True
passport = False

print("At least has one identity:",nira or passport)

print("Do not write true:", not False)

is_admin=False

print("No need admin permission:", not is_admin)

has_ticket = True
is_adult = True
is_with_his_parents = False

print("Can enter the show:",has_ticket and (is_with_his_parents or is_adult))

score = 76

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 70 and score <= 90:
    print("Grade B")
elif score >= 50 and score <= 70:
    print("Grade D")
else:
    print("Grade C")

if has_ticket:
    print("Welcome to show")

if not is_admin:
    print("You are not admin")

is_admin = True

if is_admin:
    print("Welcome to admin panel")

user = None

if not user:
    print("Status: 401 Message: Unauthorized")

user = 1

if user:
    print("Welcome user panel")


is_a_member = True
is_a_staff = False

if is_a_member:
    print('Welcome to program')
    if not is_a_staff:
        print('This is staffs room you do not have permission to enter.')
    else:
        print('Hi welcome to staff members')
else:
    print('You need a membership.') 