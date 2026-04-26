numbers = list(range(10))

print(numbers[::2])

# Reverse using negative slice
print(numbers[::-1])

for number in range(3,8):
    print(number)

for index,value in enumerate(['love','code','learn','program']):
    print(index,value)

person = {"name":"ahmed","age":34}

for key,value in person.items():
    print(key,value)