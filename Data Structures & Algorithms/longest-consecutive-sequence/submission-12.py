class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                curr = num + 1
                counter = 1
                while curr in nums_set:
                    counter += 1
                    curr += 1
            
                max_len = max(max_len, counter)
        
        return max_len