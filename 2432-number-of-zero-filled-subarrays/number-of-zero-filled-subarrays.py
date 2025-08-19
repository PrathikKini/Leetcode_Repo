class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        current_zero_subarray = total_zero_subarray = 0
        for num in nums:
            if num == 0:
                current_zero_subarray += 1
                total_zero_subarray+=current_zero_subarray
            else:
                current_zero_subarray = 0
        return total_zero_subarray