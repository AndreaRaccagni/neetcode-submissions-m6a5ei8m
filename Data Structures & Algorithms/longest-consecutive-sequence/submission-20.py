class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        
        for n in numsSet:
            if n - 1 not in numsSet:
                tmp = n
                curr = 0
                while tmp in numsSet:
                    curr += 1
                    tmp = tmp + 1
                longest = max(curr, longest)
        
        return longest
