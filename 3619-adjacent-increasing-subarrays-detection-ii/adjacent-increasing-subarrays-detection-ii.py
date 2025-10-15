class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prevInc = 0
        inc = 1
        maxLen = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
            else:
                prevInc = inc
                inc = 1
            maxLen = max(maxLen, inc // 2, min(prevInc,inc))
        return maxLen