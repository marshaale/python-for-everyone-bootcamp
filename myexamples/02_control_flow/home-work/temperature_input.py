try:
    temperature = int(input("What is todays temperature? "))
    if temperature >= 25:
        print("Warm")
    elif temperature >= 15:
        print("Ok")
    else:
        print("Cold")
except:
    print('Numeric only is allowed.')