def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
arr2 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    x = int(input())
    arr2.append(x)
bubbleSort(arr2)
nums = [2,0,2,1,1,0]
bubbleSort(nums)
nums2 = [2,0,1]
bubbleSort(nums2)
nums3 = [0]
bubbleSort(nums3)
num4= [1]
bubbleSort(num4)



print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])
for i in range(len(arr2)):
    print ("%d" %arr2[i])
for i in range(len(nums)):
    print ("%d" %nums[i])
for i in range(len(nums2)):
    print ("%d" %nums2[i])
for i in range(len(nums3)):
    print ("%d" %nums3[i])
for i in range(len(num4)):
    print ("%d" %num4[i])
#O(n)
#O(n^2)
#О(n2)
#O(1)
