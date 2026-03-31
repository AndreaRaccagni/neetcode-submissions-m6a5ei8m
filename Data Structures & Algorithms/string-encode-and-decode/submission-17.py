class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded


    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        decoded = []

        while r < len(s):
            if s[r] == '#':
                lenWord = int(s[l:r])
                wordEnd = r + 1 + lenWord
                decoded.append(s[r + 1:wordEnd])
                l = wordEnd
                r = wordEnd
            else:
                r += 1
        
        return decoded