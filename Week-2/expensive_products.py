#question #2: Expensive products

prices = [120, 45, 300, 85, 150] #demo price list
expensive = []
def get_expensive_products(prices):
    for i in prices:
        if i > 100:
            expensive.append(i)
    return expensive
print(get_expensive_products(prices))