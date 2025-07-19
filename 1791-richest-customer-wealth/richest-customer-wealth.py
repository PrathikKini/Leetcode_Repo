class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for i in accounts:
            total_sum = sum(i)
            max_sum = max(max_sum, total_sum)
        return max_sum