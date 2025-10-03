class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        num_set = set(nums)
        for num in nums:
            rev_num = int(str(num)[::-1])
            num_set.add(rev_num)
        return len(num_set)