class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = 0
        res = ''

        while p < len(word1) and p < len(word2):
            res += word1[p] + word2[p]
            p += 1

        res += word1[p:] if p < len(word1) else ''
        res += word2[p:] if p < len(word2) else ''

        return res
