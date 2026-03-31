class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestPoints = []

        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(closestPoints, (-distance, [x, y]))
            
            print(closestPoints)
            if len(closestPoints) > k:
                heapq.heappop(closestPoints)

        res = []
        for distance, points in closestPoints:
            res.append(points)

        return res