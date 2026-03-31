class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for str in strs:
            encoded += f"{len(str)}#{str}"
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        decoded = []

        while r < len(s):
            if s[r] == '#':
                wordLen = int(s[l:r])
                decoded.append(s[r + 1:r + 1 + wordLen])
                l = r + 1 + wordLen
                r = r + 1 + wordLen
            else:
                r += 1
        
        return decoded