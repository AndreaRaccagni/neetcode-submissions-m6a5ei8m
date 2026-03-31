class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        print(maxHeap)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)

            if x < y:
                y = y - x
                heapq.heappush(maxHeap, -y)
        
        return -maxHeap[0] if maxHeap else 0