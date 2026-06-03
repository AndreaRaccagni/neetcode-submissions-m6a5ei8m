class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)

        group = [[] for _ in range(n + 1)]

        for key, val in counter.items():
            group[val].append(key)

        res = []
        for i in range(n, -1, -1):
            res = res + group[i]
            if len(res) == k:
                break

        return res