class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []
        p_sum, s_sum = 0, sum(nums)
        for num in nums:
            s_sum -= num
            result.append(abs(p_sum - s_sum))
            p_sum += num
        return result