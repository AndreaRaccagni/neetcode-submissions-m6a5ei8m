class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxHeap = []

        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))

        res.append(-maxHeap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))

            while maxHeap and maxHeap[0][1] < i - k + 1:
                heapq.heappop(maxHeap)

            res.append(-maxHeap[0][0])

        return res