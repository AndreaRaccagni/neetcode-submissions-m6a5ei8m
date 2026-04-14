class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seenSums = {0: 1}
        currSum = 0
        res = 0

        for n in nums:
            currSum += n

            if currSum - k in seenSums:
                res += seenSums[currSum - k]

            seenSums[currSum] = seenSums.get(currSum, 0) + 1

        return res