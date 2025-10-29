class Solution:
    def smallestNumber(self, n: int) -> int:
        l = n.bit_length()
        c = (1 << l) - 1
        if c >= n:
            return c
        else:
            return (1 << (l+1)) - 1