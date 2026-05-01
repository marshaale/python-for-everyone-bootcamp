with open('sample.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line)

with open('sample.txt','r',encoding='utf-8') as f:
    content = f.read()
    print("Character count:",len(content))

from pathlib import Path

data = Path('sample.txt').read_text()
print(data)