numbers = [2,4,6]

for number in numbers:
    print(number*number)

for number in range(5,9):
    print(number)

# word = input("Write a word: ").strip()

# for char in word:
#     print("char in",word+":",char)

names = ["John Doe","Jane Doe","George"]

for i,name in enumerate(names):
    print("index:",i,"name:",name)

person = {"name":"Saba","age":20}

for key,value in person.items():
    print(key + ":",value)

for key in sorted(person):
    print(key + ":",person[key])

i = 0
while i < 4:
    print("i:",i)
    i +=1

total = 0
number = 1
while number != 0:
    number = int(input("Enter a number to increment total or type 0 to quit: "))
    if number != 0:
        total += number
    else:
        print("total:",total)

for n in range(20):
    print(n)
    if n == 5:
        break

for n in range(10):
    if n == 3:
        continue
    print(n)

if False:
    pass

user = {"name":"ahmed","role":"staff"}

for key in user:
    if user[key] == "staff":
        print("Access denied")
        break
    print(key,user[key])