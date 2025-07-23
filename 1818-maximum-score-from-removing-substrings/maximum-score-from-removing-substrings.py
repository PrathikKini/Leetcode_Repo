class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(s,first,second,points):
            score = 0
            stack = []
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(ch)
            return "".join(stack), score

        if x > y:
            s, score1 = remove_pairs(s,'a','b',x)
            _, score2= remove_pairs(s,'b','a',y)
        else:
            s, score1 = remove_pairs(s,'b','a',y)
            _, score2 = remove_pairs(s,'a','b',x)
        
        return score1 + score2