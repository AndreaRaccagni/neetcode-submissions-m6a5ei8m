class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        res = []

        for k, v in count.items():
            if v > n / 3:
                res.append(k)

        return res