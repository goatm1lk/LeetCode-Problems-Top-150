
#We would want to binary search here until we reach the target.
#If we don't reach target, return [-1,-1]
#Now that we have reached target, we want to check if their are any of the same targets to the right and to left.
#Once we reach a value where the next value is not the target, note down the current index. Do the same for the right side.
#Return the left and right index you had found from that search, in which it will be the range of where the targets exist in the sorted array. 

import random

def createAnArray(length):
    arr = []
    for i in range(length):
        arr.append(random.randint(0,10))
    return arr
def findRangeOfRepeatingValues(nums, target):
    nums = sorted(nums)
    l,r = 0, len(nums) -1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            startRange = mid
            endRange = mid
            while startRange > 0 and nums[startRange - 1] == target:
                startRange -= 1
            while endRange < len(nums) - 1 and nums[endRange + 1] == target:
                endRange += 1
            return [startRange, endRange,nums]
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return [-1,-1]
result = (findRangeOfRepeatingValues(createAnArray(15),random.randint(0,10)))

print(result)