class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        f, l = 0, len(s)
        res = []
        for c in s:
            if c == 'I':
                res.append(f)
                f+=1
            else:
                res.append(l)
                l-=1
        res.append(f)
        return res