class Solution:
    def isBalanced(self, num: str) -> bool:
        e = o = 0
        for i,digit in enumerate(num):
            if i % 2 == 0:
                e+=int(digit)
            else:
                o+=int(digit)
        return e == o