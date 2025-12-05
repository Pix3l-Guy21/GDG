#Question #11: Square root calculator

while 1:
    num = int(input("Enter a number: "))
    r = num/2
    l = 0
    sqrt = 0
    if r * r == num:
        sqrt = r
    else:
        while r - l > 1:
            sqrt = l + (r - l)/2
            if sqrt * sqrt < num:
                l = sqrt
            elif sqrt * sqrt > num:
                r = sqrt
            else:
                break
    print(int(sqrt))
    c = input("Continue? (y/n)")
    if c == 'n':
        break