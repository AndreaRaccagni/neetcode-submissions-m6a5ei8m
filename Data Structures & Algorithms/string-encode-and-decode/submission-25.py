class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        res = []

        while r < len(s):
            if s[r] == '#':
                word_length = int(s[l : r])
                word = s[r + 1 : r + 1 + word_length]
                res.append(word)
                l = r + 1 + word_length
                r = r + 1 + word_length

            r += 1

        return res