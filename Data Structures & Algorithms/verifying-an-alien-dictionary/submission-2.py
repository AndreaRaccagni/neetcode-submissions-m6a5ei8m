class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        mapChar = {}
        for i, c in enumerate(order):
            mapChar[c] = i
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j == len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:       
                    if mapChar[words[i][j]] > mapChar[words[i + 1][j]]:
                        return False
                    break
    
        return True
            