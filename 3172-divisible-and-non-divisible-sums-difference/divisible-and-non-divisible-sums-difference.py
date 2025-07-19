class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num2 = sum([i for i in range(1,n+1) if i % m == 0])
        num1 = sum([i for i in range(1,n+1) if i % m != 0])
        return num1 - num2
        