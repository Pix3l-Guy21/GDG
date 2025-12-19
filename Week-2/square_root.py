#Question #11: Square root calculator

num = int(input("Enter a number: "))
def sqrt(num):
    r = num/2
    l = 0
    root = 0
    if r * r == num:
        root = r
    else:
        while r - l > 1:
            root = l + (r - l)/2
            if root * root < num:
                l = root
            elif root * root > num:
                r = root
            else:
                break
    print(int(root))

sqrt(num)