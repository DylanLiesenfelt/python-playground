def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
            
arr = [156,546,878,456,456,156,156,516,515,8,87,87,561,35,9,58,7465,1,654,8789,765,165,489,785,46,9,94,531,3514,84,95,631,85649,81,200,21,5,561]

bubbleSort(arr)
print("Sorrted Array:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
