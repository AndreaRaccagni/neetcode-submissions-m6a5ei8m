class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        freqSort = [[] for _ in range(len(nums) + 1)]
            
        for n, occ in count.items():
            freqSort[occ].append(n)

        res = []
        for i in range(len(freqSort) - 1, 0, -1):
            for n in freqSort[i]:
                res.append(n)

            if len(res) == k:
                break
        
        return res
