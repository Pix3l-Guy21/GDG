#Question 10: palindrome checker

num = 32342093839024323 #demo number 
arr = [] 
i = 0 #for the numeric method

#Numeric Method without converting to string
# def isPalindrome(num):
#     if num < 0:
#         print('false')
#     else:
#         while num > 0:
#             arr.append(int(num % 10))
#             num = int(num/10) 
#         j = len(arr)-1
#         while i != j:
#             if arr[i] != arr[j]:
#                 print('false')
#                 break
#             i += 1
#             j -= 1
#         if i == j:
#             print('true')

#With change to string
def isPalindrome(num):
    num_str = str(num)
    for i in range(int(len(num_str)/2)):
        if num_str[i] != num_str[len(num_str)-i-1]:
            print('false')
            return
    print('true')

isPalindrome(num)