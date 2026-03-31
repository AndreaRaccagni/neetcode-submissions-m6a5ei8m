class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s

        return encoded

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        decoded = []

        while r < len(s):
            if s[r] == '#':
                word_len = int(s[l:r])
                decoded.append(s[r + 1 : r + word_len + 1])
                r = r + 1 + word_len
                l = r
            else:
                r += 1
        
        return decoded