#question #1: Shop discount

items = int(input("Enter number of items: "))

def discount(item):
    if item > 3:
        print("Discount applied")
    else:
        print("No discount")

discount(items)
