def bubbleSort(arr):
    n = len(arr)

    for _ in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr

def selectionSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index], arr[i]

    return arr

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]

        # first element of the sorted side ??!!!
        j = i-1 

        # move elements of arr[0...i-1]
        # greater than key, to one position ahead of their 
        # current position

        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        # first element of the unsorted side
        arr[j+1] = key
    
    return arr

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # create empty arrays
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    
    i = 0 
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)    

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()    

if __name__ == "__main__":
    this_arr = [64, 25, 12, 9, 21]

    # print(bubbleSort(this_arr))
    # print(selectionSort(this_arr))
    # print(insertionSort(this_arr))

    merge_sort(this_arr, 0, len(this_arr) - 1)

    print_list(this_arr)