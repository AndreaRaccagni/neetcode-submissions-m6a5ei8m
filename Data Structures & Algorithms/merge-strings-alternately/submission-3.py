class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = 0
        res = []

        while p < len(word1) and p < len(word2):
            res.append(word1[p])
            res.append(word2[p])
            p += 1

        res.append(word1[p:])
        res.append(word2[p:])

        return ''.join(res)
