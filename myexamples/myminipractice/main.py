with open('sample.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line)

with open('sample.txt','r',encoding='utf-8') as f:
    content = f.read()
    print("Character count:",len(content))

from pathlib import Path
import datetime
data = Path('sample.txt').read_text()
print(data)

with open('greeting.txt','w',encoding='utf-8') as f:
    f.write('Marshaale\n')
    f.write(str(datetime.datetime.now()))

with open('log.txt','a',encoding='utf-8') as f:
    f.write('Marshaale\n')

with open('log.txt','a',encoding='utf-8') as f:
    f.write('Marshaale\n')

with open('log.txt','r',encoding='utf-8') as f:
    print(f.read())

# W wipes previous content or overrides and write.
# A adds previous previous and new content.


while True:
    try:
        number = int(input('Enter a number: '))
        break
    except:
        print('Please enter a number')

try:
    with open('exercises.txt','r',encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('File exercises.txt does not exists')
finally:
    print('Completed file reading')