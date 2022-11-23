str = input("Please enter the value of the string: ")
if len(str) <= 2:
    print("Error! Please check amount of symbols in the string")
else:
    print(str[1:-1])