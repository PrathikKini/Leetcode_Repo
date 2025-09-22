class Solution:
    def minLength(self, s: str) -> int:
        res = []
        for c in s:
            res.append(c)
            if len(s) >= 2 and ("".join(res[-2:]) in ("AB","CD")):
                res.pop()
                res.pop()
        return len("".join(res))