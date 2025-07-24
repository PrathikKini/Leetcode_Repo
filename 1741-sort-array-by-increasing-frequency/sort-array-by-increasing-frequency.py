class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        countnum = {}
        for num in nums:
            countnum[num] = 1 + countnum.get(num,0)
        return sorted(nums, key=lambda x : (countnum[x], -x))