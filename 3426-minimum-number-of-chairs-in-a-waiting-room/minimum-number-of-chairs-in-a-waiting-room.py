class Solution:
    def minimumChairs(self, s: str) -> int:
        while "LE" in s:
            s = s.replace("LE",'')
        s = s.replace("L","")
        return len(s)