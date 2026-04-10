class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeight = 0
        totalWeight = 0

        for w in weights:
            maxWeight = max(maxWeight, w)
            totalWeight += w

        l = maxWeight
        r = totalWeight

        while l < r:
            mid = (r - l) // 2 + l
            
            currDays = self.computeDays(weights, mid)

            if currDays <= days:
                r = mid
            else:
                l = mid + 1
        
        return l

    def computeDays(self, arr: List[int], capacity: int) -> int:
        days = 1
        currCapacity = 0

        for w in arr:
            if currCapacity + w <= capacity:
                currCapacity += w
            else:
                currCapacity = w
                days += 1   
        
        return days