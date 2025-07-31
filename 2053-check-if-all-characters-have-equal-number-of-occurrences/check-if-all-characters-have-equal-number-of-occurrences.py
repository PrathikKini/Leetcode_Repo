class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for i in s:
            freq[i] = 1 + freq.get(i,0)
        return len(set(v for v in freq.values())) == 1