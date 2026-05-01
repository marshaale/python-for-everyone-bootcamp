with open('example.txt','r',encoding='utf-8') as file:
    content = file.read()
    print(content)

with open('example.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line)
    
with open('example.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)

with open('intro.txt','w',encoding='utf-8') as f:
    f.write("Hi aisha\n")
    f.write("Welcome to course")

with open('intro.txt','r',encoding='utf-8') as f:
    print(f.read())

with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, file!\n")

with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read())

with open('log.txt','a',encoding='utf-8') as f:
    f.write('ERROR: Api key is missing\n')
    f.write('INFO: token expired\n')
    f.write('WARNING: datetime')


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print("Zero division error")
    finally:
        print('Script completed')

print(divide(2,4)) 
print(divide(4,0))
