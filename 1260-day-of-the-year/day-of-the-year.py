class Solution:
    def dayOfYear(self, date2: str) -> int:
        from datetime import date
        y,m,d = map(int, date2.split('-'))
        return (date(y,m,d) -date(y,1,1)).days+1