def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l)-1
    
    if high < low:
        return -1


    midpoint = (low + high) // 2


    #know you are dumbass!! midpoint and l[midpoint] zzz
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__ == "__main__":    
    my_l = [9, 11, 16, 19, 101, 303]
    target = 303
    print(binary_search(my_l, target))
