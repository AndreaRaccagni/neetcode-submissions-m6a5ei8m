class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_rate = r

        while l <= r:
            mid = (r + l) // 2
            curr_rate = 0
            for pile in piles:
                curr_rate += math.ceil(pile / mid)
            
            if curr_rate <= h:
                min_rate = min(min_rate, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_rate
        