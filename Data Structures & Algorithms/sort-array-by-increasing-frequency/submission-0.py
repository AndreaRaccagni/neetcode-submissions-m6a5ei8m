class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        
        minHeap = []
        
        for n, occ in count.items():
            heapq.heappush(minHeap, (occ, -n))

        res = []
        while minHeap:
            occ, n = heapq.heappop(minHeap)
            for _ in range(occ):
                res.append(-n)

        return res