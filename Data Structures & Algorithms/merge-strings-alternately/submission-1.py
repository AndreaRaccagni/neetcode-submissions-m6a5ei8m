class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = len(word1), len(word2)
        res = []
        for i in range(max(w2, w1)):
            if i < w1:
                res.append(word1[i])
            if i < w2:
                res.append(word2[i])
        return "".join(res)
