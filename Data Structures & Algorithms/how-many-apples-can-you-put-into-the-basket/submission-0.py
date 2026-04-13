class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        totalWeight = 0
        apples = 0
        
        for w in weight:
            if w + totalWeight > 5000:
                return apples
            else:
                totalWeight += w
                apples += 1

        return apples