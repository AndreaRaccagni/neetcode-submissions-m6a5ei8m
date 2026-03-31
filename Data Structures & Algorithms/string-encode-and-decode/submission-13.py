class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += f'{len(s)}#{s}'
        return encoded
        

    def decode(self, s: str) -> List[str]:
        decoded = []
        i, j = 0, 0

        while j < len(s):
            if s[j] != '#':
                j += 1
                continue
            
            strLen = int(s[i:j])
            start = j + 1
            j = start + strLen
            decoded.append(s[start:j])
            i = j

        return decoded