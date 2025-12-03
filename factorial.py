def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)

num = int(input("Enter a number: "))
print(f"The factorial of  {num} is {factorial(num)}")