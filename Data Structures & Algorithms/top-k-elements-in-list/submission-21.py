class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = [(-c, n) for n, c in counter.items()]
        heapq.heapify(heap)

        res = []

        while len(res) < k:
            c, n = heapq.heappop(heap)
            res.append(n)

        return res
