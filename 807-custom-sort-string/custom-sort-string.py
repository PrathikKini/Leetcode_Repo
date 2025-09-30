class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        
        result = []
        for ch in order:
            if ch in freq:
                result.append(ch * freq[ch])
                del freq[ch]
        
        for ch, cnt in freq.items():
            result.append(ch * cnt)

        return "".join(result)
