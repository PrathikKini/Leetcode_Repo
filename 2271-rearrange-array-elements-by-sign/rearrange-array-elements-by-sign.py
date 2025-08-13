class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pi = 0
        ni = 1
        res = [0] * len(nums)
        for num in nums:
            if num > 0:
                res[pi] = num
                pi+=2
            else:
                res[ni] = num
                ni+=2
        return res
                