class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def do_sum(idx : int) -> int:
            ctr = Counter(nums[idx:idx + k])
            most_freq = nlargest(x, ctr, key = lambda y : (ctr[y], y))
            return sum(map(lambda y:y * ctr[y], most_freq))
        
        return list(map(do_sum, range(len(nums)+1 - k)))