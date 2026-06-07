class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        negative = num < 0
        num = abs(num)
        res = []

        while num:
            res.append(str(num%7))
            num //= 7
        
        ans = ''.join(reversed(res))
        return '-' + ans if negative else ans
