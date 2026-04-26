line = ""

while line != 'done':
    line = input("Write a word or write 'done' to exit: ").strip().lower()
    if line != 'done':
        print('You typed:',line)
    else:
        print("Goodbye!")  