def total(*numbers):
    return sum(numbers)

print("Sum of 1,3,4,5 is:",total(1,3,4,5))
print("Sum of 1,4,10 is:",total(1,4,10))
print(total())

def profile(**info):
    for key,value in info.items():
        print(f"{key}: {value}")

profile(theme="light",username="ahmed",email="a@example.com")
print(' ')
profile(balance=112,card_number="******* 027",expires='03/31')