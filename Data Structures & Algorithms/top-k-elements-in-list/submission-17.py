class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = {}

        for n in nums:
            numsCount[n] = numsCount.get(n, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]


        for n, occ in numsCount.items():
            buckets[occ].append(n)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
