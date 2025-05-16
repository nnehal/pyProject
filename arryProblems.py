def moveZero(arr):
    count= 0
    l= len(arr)

    for i in range(l):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
    return arr

def secondLargest(arr):
    largest = -1
    second_largest = -1

    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i < largest and i > second_largest:
            second_largest = i
    return second_largest

def reverseArray(arr):
    
    arr = arr[::-1]

    return arr

def rotateArray(arr, d):
    import math
    
    n= len(arr)
    d %= n

    cycles = math.gcd(n, d)

    for i in range(cycles):
        startEle = arr[i]
        currIdx= i

        while True:
            nextIdx= (currIdx + d) % n

            if nextIdx == i:
                break

            arr[currIdx] = arr[nextIdx]
            currIdx = nextIdx

        arr[currIdx] = startEle
    
    return arr

def recursivePermutation(index, s, ans):
    if index == len(s):
        ans.append("".join(s))
        return
    
    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]
        recursivePermutation(index + 1, s, ans)
        s[index], s[i] = s[i], s[index]

def findPermutation(s):
    ans= []

    recursivePermutation(0, list(s), ans)

    ans.sort()

    return ans

def majorityElement(arr):
    count= 0
    candidate= -1

    for num in arr:
        if count == 0:
            candidate= num
            count += 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    count = 0

    for num in arr:
        if num == candidate:
            count += 1

    if count > len(arr) // 2:
        return candidate
    else:
        return -1
    
def maxArraySum(arr):
    result= arr[0]
    maxEnding= arr[0]
    l= len(arr)

    for i in range(1, l):
        maxEnding= max(maxEnding + arr[i], arr[i])
        result= max(maxEnding, result)

    return result


    pass
if __name__ == "__main__":
    my_list = [1,2,3,2,2,2,4]
    # print(rotateArray(my_list, 3))
    mix= [2, 3, -8, 7, -1, 2, 3]

    word= "ABC"

    print(maxArraySum(mix))
