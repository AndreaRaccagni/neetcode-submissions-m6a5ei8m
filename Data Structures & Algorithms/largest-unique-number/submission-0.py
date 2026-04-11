class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = {}
        largest = -1

        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        for n, occ in counter.items():
            if occ == 1:
                largest = max(n, largest)

        return largest