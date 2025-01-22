def TwoSum(nums, target):
    n = len(nums)
    numMap = {}

    for i in range(n):
        complement = target - nums[i]

        if complement in numMap:
            return [numMap[complement], i]
        
        numMap[nums[i]] = i
    return []





def removeDuplicates(nums):
    j = 1

    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1

    return j

def removeElements(nums, val):

    index = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index

def searchInsertPos(nums, val):
    left = 0
    right = len(nums) -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == val:
            return mid
        elif nums[mid] > val:
            right = mid -1
        else:
            left = mid + 1

    return left

def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


def mergeSortedArray(nums1, m, nums2, n):
    midx = m-1
    nidx = n-1
    right = m+n-1

    while nidx >=0:
        if midx >=0 and nums1[midx] > nums2[nidx]:
            nums1[right] = nums1[midx]
            midx -= 1
        else:
            nums1[right] = nums2[nidx]
            nidx -= 1

        right -= 1

def arrayToBinaryTree(arr): 
    pass

def bestPrice(prices):
    min_price = float('inf')
    max_price = 0
    max_profit = 0

    for price in prices:
        if min_price < price:
            min_price = price
            
            profit =abs(max_price - min_price)

            if profit > max_profit:
                max_profit = profit
    return max_profit



# prices = [7,1,5,3,6,4]
my_list1 = [1,2,3,4,0,0]
# my_list2 = [5,6]
nums = [3,2,4]
# print(searchInsertPos(my_list, 4))
# # print(my_list)

print(TwoSum(nums, 6))