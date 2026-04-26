class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        
        for n, count in counter.items():
            buckets[count].append(n)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                res.append(n)

            if len(res) == k:
                return res

        return res