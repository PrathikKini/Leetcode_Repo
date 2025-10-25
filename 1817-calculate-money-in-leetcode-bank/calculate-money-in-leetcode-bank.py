class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        r = n % 7
        sum_weeks = 28 * w + 7 * (w * (w - 1) // 2)
        sum_rem = r * (2 * (1 + w) + (r - 1)) // 2
        return sum_weeks + sum_rem