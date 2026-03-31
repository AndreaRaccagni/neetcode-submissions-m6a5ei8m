class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        maxCount = max(list(counter.values()))
        buckets = [[] for _ in range(maxCount)]

        for key, value in counter.items():
            buckets[value - 1].append(key)

        res = []

        for i in range(maxCount - 1, -1, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
            

