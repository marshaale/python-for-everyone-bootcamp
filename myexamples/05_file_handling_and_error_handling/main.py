with open('example.txt','r',encoding='utf-8') as file:
    content = file.read()
    print(content)

with open('example.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line)
    
with open('example.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)