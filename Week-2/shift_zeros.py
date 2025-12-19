#Question #8: move zeros to end

#demo array
arr = []
def zeroShifter(arr):
    if len(arr) > 1:
        for i in range(len(arr)):
            if arr[i] == 0:
                for j in range(i+1, len(arr)):
                    arr[j-1] = arr[j]
                arr[-1] = 0
    print(arr)

zeroShifter(arr)