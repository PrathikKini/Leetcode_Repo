class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first = second = float('-inf')
        idx = -1
        for i, num in enumerate(nums):
            if num > first:
                second = first
                first = num
                idx = i
            elif num > second and num != first:
                second = num

        if first >= second * 2:
            return idx
        return -1