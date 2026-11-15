class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            time = self.hoursToEatBananas(mid, piles)

            if time > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
    
    def hoursToEatBananas(self, mid: int, piles: List[int]) -> int:
        res = 0
        for p in piles:
            res += math.ceil(p / mid)
        return res