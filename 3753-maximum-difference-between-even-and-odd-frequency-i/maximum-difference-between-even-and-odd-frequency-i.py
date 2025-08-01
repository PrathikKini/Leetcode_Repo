class Solution:
    def maxDifference(self, s: str) -> int:
        d = dict(Counter(s))
        odd = [v for v in d.values() if v%2!=0]
        even = [v for v in d.values() if v%2==0]
        if not odd or not even:
            return 0

        res = max([o-e for o in odd for e in even])
        return res