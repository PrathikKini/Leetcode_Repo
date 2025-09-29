class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for i in range(1,len(nums),2):
            total = total + min(nums[i-1],nums[i])
        return total