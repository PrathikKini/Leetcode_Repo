class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        prefix_sum = [0] * (n+1)

        for i, num in enumerate(nums):
            prefix_sum[i+1] = prefix_sum[i] + num
            total_sum += prefix_sum[i+1] - prefix_sum[max(0, i - num)]

        return total_sum