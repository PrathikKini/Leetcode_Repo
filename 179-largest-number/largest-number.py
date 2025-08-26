class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        array_list = list(map(str,nums))
        array_list.sort(key = lambda x: x*10, reverse=True)
        if array_list[0]=="0":
            return '0'
        return "".join(array_list)