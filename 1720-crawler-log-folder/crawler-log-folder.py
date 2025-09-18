class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c = 0
        for l in logs:
            c+= {"../":-1,"./":0}.get(l,1)
            c = max(c,0)
        return c