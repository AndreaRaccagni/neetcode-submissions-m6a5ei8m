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
                length = int(s[l : r])
                start = r + 1
                end = start + length
                word = s[start : end]
                decoded.append(word)
                l = end
                r = l
            r += 1

        return decoded