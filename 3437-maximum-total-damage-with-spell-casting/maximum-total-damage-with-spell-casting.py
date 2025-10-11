class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq)
        n = len(keys)
        dp = [0] * n
        dp[0] = freq[keys[0]] * keys[0]
        for i in range(1, n):
            take = freq[keys[i]] * keys[i]
            l, r, ans = 0, i-1, -1
            while l <= r:
                m = (l+r) // 2
                if keys[m] <= keys[i] - 3:
                    ans = m
                    l = m + 1
                else:
                    r = m - 1
            if ans >= 0:
                take += dp[ans]
            dp[i] = max(dp[i-1], take)
        return dp[-1]