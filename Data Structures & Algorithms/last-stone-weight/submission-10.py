class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for s in stones:
            heapq.heappush(maxHeap, -s)

        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)

            if x == y:
                continue

            heapq.heappush(maxHeap, y - x)
        
        return -maxHeap[0] if maxHeap else 0