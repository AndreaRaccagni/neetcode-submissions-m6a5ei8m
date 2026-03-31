class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []

        for num in nums:
            heapq.heappush(maxHeap, -num)

        for i in range(k):
            res = -heapq.heappop(maxHeap)
        return res
