age = int(input("Enter your age: "))
if age >= 13:
    print("Ok to enter")
elif age <= 10:
    has_parent_or_guardian = input("is a parent or guardian is with you? (y/n) ").lower()
    if has_parent_or_guardian == "y":
        print("Ok to enter")
    else:
        print("Sorry, not this time")
else:
    print("Sorry, not this time")