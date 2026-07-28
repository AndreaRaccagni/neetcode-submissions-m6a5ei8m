class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = []
        res = nums[:]

        for i in range(len(nums)):
            heapq.heappush(minHeap, (nums[i], i))

        for _ in range(k):
            n, index = heapq.heappop(minHeap)
            n = n * multiplier
            heapq.heappush(minHeap, (n, index))
            res[index] = n

        return res