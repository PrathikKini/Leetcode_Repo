class Solution:
    def isFascinating(self, n: int) -> bool:
        return ''.join(sorted(f'{n}{2*n}{3*n}')) == '123456789'