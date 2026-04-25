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