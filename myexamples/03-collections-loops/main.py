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