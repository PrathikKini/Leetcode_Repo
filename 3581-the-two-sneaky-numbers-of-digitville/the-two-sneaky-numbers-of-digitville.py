class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        countr = Counter(nums)
        return [itm for itm, cnt in countr.items() if cnt > 1]