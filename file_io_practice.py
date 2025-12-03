# with open("test.txt", "w") as file:
#     file.write("Bamlak")
try:
    with open("test.txt", "r") as file:
        content = file.read()
        print(f"Welcome {content}")
except:
    with open("test.txt", "w") as file:
        file.write("Guest")
finally:
    with open("test.txt", "r") as file:
        content = file.read()
        print(f"Welcome {content}")