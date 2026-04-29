class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for s in stones:
            heapq.heappush(minHeap, -s)

        while len(minHeap) > 1:
            y = heapq.heappop(minHeap)
            x = heapq.heappop(minHeap)
            if x > y:
                newStone = y - x
                heapq.heappush(minHeap, newStone)

        return -minHeap[0] if minHeap else 0