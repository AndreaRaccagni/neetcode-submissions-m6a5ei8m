class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            d = x * x + y * y
            heapq.heappush(minHeap, (-d, [x, y]))

            while len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []

        for _, coordinates in minHeap:
            res.append(coordinates) 
        
        return res
                