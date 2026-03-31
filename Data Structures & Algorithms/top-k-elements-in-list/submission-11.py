class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        sortFreq = [[] for i in range(len(nums) + 1)]

        for num, freq in count.items():
            sortFreq[freq].append(num)
        
        res = []

        for i in range(len(nums) - 1, -1, -1):
            for num in sortFreq[i + 1]:
                if len(res) == k:
                    return res

                res.append(num)

        return res