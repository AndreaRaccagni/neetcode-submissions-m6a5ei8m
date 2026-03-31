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

            strsMap[hashedStr] = strsMap.get(hashedStr, []) + [s]

        return list(strsMap.values())

