class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(maxHeap, (-distance, [x, y]))

            print(maxHeap)

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

            print(maxHeap)

        res = []
        while maxHeap:
            distance, coordinates = heapq.heappop(maxHeap)
            res.append(coordinates)

        return res