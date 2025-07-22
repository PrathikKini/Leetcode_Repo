class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique_elements = set()
        left = curr_sum = max_sum = 0
        for right in range(len(nums)):
            while nums[right] in unique_elements:
                unique_elements.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            unique_elements.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)
        return max_sum