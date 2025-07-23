class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        else:
            min_val = min(nums)
            max_val = max(nums)
            nums.remove(min_val)
            nums.remove(max_val)
        return nums[0]