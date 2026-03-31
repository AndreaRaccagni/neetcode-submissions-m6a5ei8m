class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}
        for i in range(len(order)):
            orderMap[order[i]] = i

        for i in range(len(words) - 1):
            m = len(words[i])
            n = len(words[i + 1])
            minLen = min(m, n)
            sameChars = 0

            for j in range(minLen):
                if orderMap[words[i][j]] < orderMap[words[i + 1][j]]:
                    break
                elif orderMap[words[i][j]] > orderMap[words[i + 1][j]]:
                    return False
                else:
                    sameChars += 1
            
            if sameChars == minLen and n < m:
                return False

        return True