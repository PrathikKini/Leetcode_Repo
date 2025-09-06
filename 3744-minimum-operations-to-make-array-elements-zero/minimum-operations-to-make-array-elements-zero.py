class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for q in queries:
            s, e = q
            ops = 0
            prev = 1

            for d in range(1,17):
                cur = prev * 4
                l = max(s, prev)
                r = min(e, cur-1)

                if r >= l:
                    ops += (r-l+1) *d
                prev = cur

            ans += (ops + 1) //2
        return ans