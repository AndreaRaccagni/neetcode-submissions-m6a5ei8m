class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        min_rate = 1
        res = max(piles)

        while min_rate <= max_rate:
            k = (min_rate + max_rate) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours > h:
                min_rate = k + 1
            else:
                max_rate = k - 1
                res = k
     
        return res
