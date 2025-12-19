nums = [3, 5, 6, 2, 10, 40, 20, 1, 5, 29, 20, 43, 20]

#custom list
# nums = []
# listLength = int(input("Enter list size: "))
# for i in range(listLength):
#   num = int(input("Enter a number: "))
#   nums.append(num)

max = nums[0]
for i in nums:
    if max < i:
        max = i

print(f"The maximum number from the list is: {max}")