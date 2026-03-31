class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []

        r = 0
        l = 0

        while r < len(s):
            if s[r] == '#':
                wordLen = int(s[l : r])
                word = s[r + 1 : r + 1 + wordLen]
                res.append(word)
                r += 1 + wordLen
                l = r
            else:
                r += 1
        
        return res