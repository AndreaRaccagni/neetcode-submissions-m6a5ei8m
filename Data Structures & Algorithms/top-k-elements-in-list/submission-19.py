class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        counter = Counter(nums)

        for n, c in counter.items():
            heapq.heappush(maxHeap, (-c, n))

        res = []

        while len(res) < k:
            c, n = heapq.heappop(maxHeap)
            res.append(n)

        return res
