print(11+5)
print(3/2)
print(3//2)
print("Hello"*3)

balance = 100

balance -= 25

balance += 10

print("Your balance is",balance)

word = "Hi"

word += " there here we are."

print(word)

score = 88
print(score >= 80)

name = "Ada"
print(name == "Ada")

username = "Alex"
is_loged_in = True

print(username == "Alex" and is_loged_in)

day = "Monday"
print("Is weekend:",day == "Sundany" or day == "Saturday")

temprature = 30

if temprature >= 25:
    print("Warn")
elif temprature >= 15:
    print("Ok")
else:
    print("Cold")

user_role = input("Entre your role: ")
if user_role == "admin":
    password = input("Enter password: ")
    if password == "secret":
        print("Access Granted")
    else:
        print("Wrong password")
else:
    print("Unknown role")