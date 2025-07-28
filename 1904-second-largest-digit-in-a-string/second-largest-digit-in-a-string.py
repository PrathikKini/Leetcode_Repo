class Solution:
    def secondHighest(self, s: str) -> int:
        first = -1
        second = -1
        for c in s:
            if c.isdigit():
                d = ord(c) - ord('0')
                if d > first:
                    second = first
                    first = d
                elif d > second and d < first:
                    second = d
        return second