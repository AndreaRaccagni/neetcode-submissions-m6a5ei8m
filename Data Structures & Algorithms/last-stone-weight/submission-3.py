class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            diff = y - x

            if diff > 0:
               heapq.heappush(maxHeap, -diff)

        return -maxHeap[0] if len(maxHeap) else 0