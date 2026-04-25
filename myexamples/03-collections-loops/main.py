scores = [80,75,90,100,50]
print(len(scores))
print(scores[-1])

print(scores[0])
print(scores[1])

print(scores[1:4])

print(scores)

scores.append(88)
scores.insert(1,95)

print(scores)

scores.remove(50)
scores.pop(0)

print(scores)

scores.extend([65,58])

print(scores)

print(scores[:])

print(scores[1:])

print(scores[:4])

print(scores[0:4:2])

points = (75,88)

print(points[0],points[1])

x,y = points

print("X=",x,"Y=",y)

print(type(points))

single_tuple = (66,)
print(type(single_tuple))

tags = {"python","code","learn","python","js","ts"}
print(tags)

tags.add("fun")
# tags.remove('java')
tags.discard('java')

print(tags)

print("fun" in tags)

python = {"oop","interpreter","class","type dynamic"}
java = {"oop","compiler","class","type safe"}

print(python)
print(java)

print("Python union java",python | java)
print("Python intersect java",python & java)
print("Python difference java",python - java)
print("Java difference Python",java - python)

a = {1, 2, 3}
b = {3, 4, 5}

print("A union B",a | b)
print(a-b)
print(a&b)

person = {"name":"Maria","age":19}

print(person)

print(person["name"])
print(person.get("age"))
print(person.get("nationality","somalia"))

person["nationality"] = "italy"

print(person.get("nationality","somalia"))

# print(person["dob"])

del person["nationality"]
person.pop("age")

print(person)

student = {"name":"Morgan","dob":2000,"address":{"city":"London","street":"124 KM House"},"scores":[95,88,67,79,82,100]}

print(student["name"])

print(student.get("email","no email"))

student["email"] = "morgan@example.com"

print(student)
print("keys",len(student.keys()))
print("Values",len(student.values()))

print(type(student))

numbers = [1,2,3,4]
# print each number in numbers
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
# This is one of the problem loop solves
for number in numbers:
    print(number)

for x in range(1,3):
    print(x)

colors = ["red", "blue", "green"]
for color in colors:
    print("Color",color)

for char in "Hi!":
    print(char)

for i,number in enumerate(numbers):
    print("index:",i,"number:",number)

for i,color in enumerate(colors,1):
    print("index:",i,"color:",color)

mobile = {"name":"Samsung a10","year":2020,"type":"a series"}

for key,value in mobile.items():
    print(key,value)

for key in mobile:
    print(mobile[key])

dataset = ((0,1,0),(1,1,0),(0,0,1))

for a,b,c in dataset:
    print(a,b,c)

number = 1
while number <= 3:
    print("number =",number)
    number += 1

line = ""
while line != "done":
    line = input("type a word, or 'done' to stop: ").strip().lower()
    if line != "done":
        print("You said:",line,"and it's length is:",len(line))

for x in range(5):
    pass

for i in [0,1,2,3,4]:
    if i == 1:
        print("Loop skips index:",i)
        continue

    if i == 3:
        print("Loop stopped at index:",i)
        break

    print("index:",i)
print("Full indexes",[0,1,2,3,4])