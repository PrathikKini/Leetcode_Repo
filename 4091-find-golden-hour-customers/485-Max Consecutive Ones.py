# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 
def findMaxConsecutiveOnes(nums):
    max_count = 0
    count = 0
    
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
            
    return max_count

# Test cases
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))  # Output: 3
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))  # Output: 2  