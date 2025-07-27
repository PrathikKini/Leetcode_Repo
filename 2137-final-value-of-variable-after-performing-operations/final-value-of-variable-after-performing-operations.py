class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if '++' in inp else -1 for inp in operations)