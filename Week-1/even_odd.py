while 1:
    num = int(input("Enter a number: "))

    if num % 2:
        print("The number is Odd")
    else:
        print("The number is Even")
    cont = input("Do you want a redo? (y/n) default(y)")
    if cont == "n" or cont == "N":
        break