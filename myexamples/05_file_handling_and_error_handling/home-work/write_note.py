with open('note.txt','w',encoding='utf-8') as f:
    f.write('Remember: paying bills\n')
    f.write('Do not miss to pay bills tomorrow morning.\n')

with open('note.txt','r',encoding='utf-8') as f:
    print(f.read())