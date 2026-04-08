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

            currDays = self.findDays(weights, mid)

            if currDays <= days:
                r = mid
            else:
                l = mid + 1

        return l

    def findDays(self, arr, capacity):
        days = 1
        batch = 0

        for w in arr:
            if batch + w <= capacity:
                batch += w
            else:
                days += 1
                batch = w

        return days
