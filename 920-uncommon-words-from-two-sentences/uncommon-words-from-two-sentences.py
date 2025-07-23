class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s3 = s1.split() + s2.split()
        s3_count = {}
        for word in s3:
            s3_count[word] = 1 + s3_count.get(word,0)
        return [k for k, v in s3_count.items() if v == 1]