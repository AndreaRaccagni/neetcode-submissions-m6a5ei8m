class Solution:
    def maxDepth(self, s: str) -> int:
        maxP = 0
        currP = 0
        
        for c in s:
            if c == '(':
                currP += 1
                maxP = max(maxP, currP)
            elif c == ')':
                currP -= 1

        return maxP