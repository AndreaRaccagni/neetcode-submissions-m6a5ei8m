class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            k = (r + l) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / k)

            if totalTime > h:
                l = k + 1
            else:
                r = k

        return l