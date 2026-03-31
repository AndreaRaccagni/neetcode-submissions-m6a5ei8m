class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)

        for stone in stones:
            heapq.heappush(maxHeap, stone * -1)

        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap) * -1
            x = heapq.heappop(maxHeap) * -1

            if x < y:
               heapq.heappush(maxHeap, (y - x) * -1)

            print(maxHeap)

        return maxHeap[0] * -1 if len(maxHeap) else 0