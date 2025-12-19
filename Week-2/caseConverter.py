#Question #13: converting to uppercase
def toUpperCase(doc):
    try:
        with open(doc, "r+") as file:
            context = file.read()
            print(f"Current content: \n{context}\n")
            context = context.upper()
            print(f"Content will change to: \n{context}\n")
            opt = input('Do you want to apply change? (y/n)')
            if opt == 'y':
                file.seek(0)
                file.write(context)
                print("Change applied")
            else:
                print("Change discarded")
    except FileNotFoundError:
        print("File not found")
        
toUpperCase('file.txt')