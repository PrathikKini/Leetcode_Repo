class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        mp = {}
        for i in range(len(t)):
            mp[t[i]] = i
        res = 0
        for i in range(len(s)):
            res+= abs(i - mp[s[i]])
        return res