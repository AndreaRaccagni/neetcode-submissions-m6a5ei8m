class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + '#' + s)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        res = []

        while r < len(s):
            if s[r] == '#':
                word_length = int(s[l:r])
                res.append(s[r + 1 : r + 1 + word_length])
                r = r + word_length
                l = r + 1
            r += 1

        return res