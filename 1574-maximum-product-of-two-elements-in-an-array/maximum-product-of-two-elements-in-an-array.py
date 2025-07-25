class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = float('-inf')
        max2 = float('-inf')
        for num in nums:
            if num >= max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return (max2-1) * (max1-1)