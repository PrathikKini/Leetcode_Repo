class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = 0
        expected = sorted(heights)

        for k, v in enumerate(heights):
            if v != expected[k]:
                cnt += 1
        return cnt