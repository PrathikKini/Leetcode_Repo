class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 1000000007
        grp = defaultdict(int)
        for _, y in points:
            grp[y] += 1
        res = total = 0
        for y, cnt in grp.items():
            lines = cnt * (cnt - 1) // 2
            res = (res + total * lines) % mod
            total = (total + lines) % mod
        return res