class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cntr = Counter([n for n in nums if n%2==0])
        if not cntr:
            return -1
        max_v = max(cntr.values())
        return min(k for k, v in cntr.items() if v == max_v)