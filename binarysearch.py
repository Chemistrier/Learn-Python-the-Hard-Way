from datetime import datetime

def binary_search(arr, x):
    start_time = datetime.now()
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            end_time = datetime.now()
            print('Funciton running time: {}'.format(end_time - start_time))
            return mid
    return -1


arr = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 ]
x = 6

result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result+1))
else:
    print("Element is not present in array")
