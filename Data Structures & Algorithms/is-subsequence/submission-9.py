class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0

        for c in t:
            if p < len(s) and s[p] == c:
                p += 1

        return p == len(s)