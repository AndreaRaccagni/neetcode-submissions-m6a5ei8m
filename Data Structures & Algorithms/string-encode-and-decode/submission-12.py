class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for str in strs:
            encoded += f'{len(str)}#{str}'
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
            stop = start + strLen
            decoded.append(s[start:stop])
            i = stop
            j = i

        return decoded