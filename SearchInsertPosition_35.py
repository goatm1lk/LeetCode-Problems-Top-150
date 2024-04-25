import random
#TODO: Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

#NOTE:
#1. First we want to create a left and right pointer for the nums array.
#2. Next we would want loop through the nums array with these pointers, calculating the mid point of the array each time. We will use this to binary search the array.
#3. Following that, we would want to check if the middle value of the nums array is less than the target, equal to the target, or greater than the target.
#If it's less than the target, move the left pointer to mid + 1, if its equal to the target, return the mid index, and if it's greater than the target move the right index to the left of the midpoint.
#4.After we loop through the whole array until the left pointer is greater than the right pointer, if there was no target found, return the left index as that is where it should be placed. 
#For example, on the last iteration if the mid value is still less than the target, then we will adjust to the right once and this will be the position, however if it is greater, then left will stay the same and the index will be placed there.



def searchInsertPostion(nums,target):
    l,r = 0,len(nums) - 1
    nums = sorted(nums)
    print("In this array, ",nums," We are looking for ",target)
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] == target:
            return mid
        else:
            r = mid - 1
    return l

def generateArray(length):
    numsArray = []
    for i in range(length):
        numsArray.append(random.randint(0,999999))
    return numsArray

nums = generateArray(10)
result = searchInsertPostion(nums,random.randint(0,999999))
print("The number will be located at index :", result) if result in nums else print("The number was not found in the nums array, the number will be inserted at index :", result)