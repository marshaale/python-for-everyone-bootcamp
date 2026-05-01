with open('sample.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    total_chars = 0
    for line in lines:
        total_chars += len(line)

    print("Lines:",len(lines))
    print("Character count:",total_chars)
