class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for s in stones:
            heapq.heappush(maxHeap, -s)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)

            if x < y:
                heapq.heappush(maxHeap, x - y)

        return -heapq.heappop(maxHeap) if maxHeap else 0

