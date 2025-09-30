class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res, ncr, n = 0, 1, len(nums) - 1
        for r, num in enumerate(nums):
            res = (res + num * ncr) % 10
            ncr = ncr * (n-r) // (r+1)
        return res