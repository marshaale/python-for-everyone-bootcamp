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