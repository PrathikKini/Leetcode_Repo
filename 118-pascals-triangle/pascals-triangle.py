class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res= [[1]]
        for i in range(1,numRows):
            res+=[list(map(lambda x,y : x+y,[0] + res[-1],res[-1] + [0]))]
        return res[:numRows]