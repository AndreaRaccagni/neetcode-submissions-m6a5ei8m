class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        strsMap = {}

        for s in strs:
            abc = [0] * 26

            for i in range(len(s)):
                index = ord(s[i]) - ord('a')
                abc[index] += 1

            hashedStr = ''
            for count in abc:
                hashedStr += f"{count}#"

            if hashedStr in strsMap:
                strsMap[hashedStr].append(s)
            else:
                strsMap[hashedStr] = [s]

        for group in strsMap.values():
            res.append(group)

        return res

