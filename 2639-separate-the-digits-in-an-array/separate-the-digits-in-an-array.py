class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.extend(int(d) for d in str(num))
        return ans