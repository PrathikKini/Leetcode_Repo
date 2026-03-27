# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]

def findDisappearedNumbers(nums):
    res = []
    idx = 0
    nums.sort()
    n = len(nums)
    for num in range(1, n + 1):
        while idx < n and nums[idx] < num:
            idx += 1
        if idx == n or nums[idx] > num:
            res.append(num)
    return res
    
# Test cases
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # Output: [5,6]
print(findDisappearedNumbers([  1,1]))  # Output: [2]  