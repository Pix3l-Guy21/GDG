#Question #9: Target sum

nums = [2,4,2,6,20,7,11,15] #demo list of numbers
target = 26 #demo target
def findIdx(arr, target):
    result=[]
    for i in range(len(arr)-1):
        j = i+1
        while j < len(arr):
            if(arr[i] + arr[j] == target):
                result.append(i)
                result.append(j)
                break
            j += 1
        if len(result):
            break
    return result
print(findIdx(nums, target))