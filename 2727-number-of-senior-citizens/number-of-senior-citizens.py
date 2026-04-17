class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for age in details:
            if int(age[11:13]) > 60:
                cnt+=1
        return cnt