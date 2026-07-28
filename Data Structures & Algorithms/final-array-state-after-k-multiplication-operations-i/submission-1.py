class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = []

        for i in range(len(nums)):
            heapq.heappush(minHeap, [nums[i], i])

        for _ in range(k):
            currMin = heapq.heappop(minHeap)
            currMin[0] = currMin[0] * multiplier
            heapq.heappush(minHeap, currMin)

        res = [0] * len(nums)
        for n, i in minHeap:
            res[i] = n

        return res