class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a','e','i','o','u'}
        vow = [0] * 26
        cons = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            if ch in vowels:
                vow[idx] += 1
            else:
                cons[idx] += 1

        return max(vow) + max(cons)
        