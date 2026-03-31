class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestPoints = []

        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(closestPoints, (-distance, [x, y]))
            
            if len(closestPoints) > k:
                heapq.heappop(closestPoints)
        
        return [points for _, points in closestPoints]