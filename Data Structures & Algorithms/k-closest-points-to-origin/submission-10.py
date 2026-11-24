class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            distance = x * x + y * y
            heapq.heappush(minHeap, (-distance, [x, y]))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        for d, coord in minHeap:
            res.append(coord)

        return res