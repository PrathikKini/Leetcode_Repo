class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        lst = []
        while nums:
            avg = sum([min(nums)+max(nums)]) / 2
            nums.remove(min(nums))
            nums.remove(max(nums))
            lst.append(avg)
        return min(lst)