class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        prefix = strs[0]

        for s in strs:
            p = 0
            while p < min(len(prefix), len(s)) and prefix[p] == s[p]:
                p += 1

            prefix = s[:p] 

        return prefix