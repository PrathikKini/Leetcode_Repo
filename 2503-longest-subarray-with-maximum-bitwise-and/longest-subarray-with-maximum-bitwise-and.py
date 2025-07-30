class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = cur = 0
        mx = max(nums)
        for num in nums:
            if num == mx:
                cur+=1
                longest = max(longest,cur)
            else:
                cur = 0
        return longest