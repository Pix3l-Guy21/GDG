#Question #5 and #6: sales number calc
#Also same logic for #12 since goal is to add only numbers in both question set
try:
    with open('sales.txt', 'r') as file:
        valid_sales = []
        total = 0
        for i in file:
            try:
                valid_sales.append(int(i))
                total += int(i)
            except ValueError:
                continue
        print(f'Total sales: {total}')
    
except:
    print('File not found')