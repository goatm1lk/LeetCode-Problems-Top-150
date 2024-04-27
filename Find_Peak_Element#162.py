import random
#Problem: 
# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

#NOTE: 
#1.We must first create left and right pointers for the array.
#Now considering that an array with the length of 1, will be a peak no matter what, as the out of bounds indexes count as 0, so if the nums length is 1 we can return 0
#If the length of the array is 2, the we have to dermine which index is larger, and return that index.
#2. For arrays, with lengths larger than 3, we must loop through this array.
#3.In this loop through the array, we need to find the midpoint of the array. Along with the value of the indexes to its left and right. If the index is out of bounds, set it to 0.
#4. Now we would want to check if our current mid point is a peak, if it is return the mid index.
#5. If not then we would want to check which index is larger, mid - 1, or mid + 1. If mid- 1 is larger we move the right pointer to the left of the mid index, and if mid + 1 is larger we move the left pointer to the right of the midpoint.


def generateNumArray(length):
    numsArray = []
    for i in range(length):
        numsArray.append(random.randint(1,99))
    return numsArray

def findPeakElements(nums):
    l,r = 0, len(nums) -1
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return 0
        else:
            return 1
    while l < r:
        mid = (l + r) // 2
        leftMid = nums[mid - 1] if nums[mid-1] is not None else 0
        rightMid = nums[mid + 1] if nums[mid + 1] is not None else 0
        if nums[mid] > leftMid and nums[mid] > rightMid:
            return mid
        else:
            if leftMid > rightMid:
                r = mid - 1
            else:
                l = mid + 1
    return l
nums = generateNumArray(10)
result = findPeakElements(nums)
print("Number List: ",nums,"Peak Number: ",nums[result])