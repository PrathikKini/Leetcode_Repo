class Solution:
    def countDigits(self, num: int) -> int:
        return sum(1 if num % int(digit) == 0  else 0 for digit in str(num))