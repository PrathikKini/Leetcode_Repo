class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year = date.split('-')[0]
        month = date.split('-')[1]
        day = date.split('-')[2]
        return bin(int(year))[2:] + '-' + bin(int(month))[2:] + '-' + bin(int(day))[2:]