class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x % sum(int(num) for num in str(x)) == 0:
            return sum(int(num) for num in str(x))
        return -1