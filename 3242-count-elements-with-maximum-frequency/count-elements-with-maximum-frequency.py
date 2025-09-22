class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        
        max_freq = max(freq.values())

        return sum(v for k,v in freq.items() if v == max_freq)

