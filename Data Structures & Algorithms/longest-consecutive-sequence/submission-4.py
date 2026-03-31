class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numsSet = set(nums)
        seen = set()
        mapConsecutive = {}

        for num in nums:
            if num in seen:
                continue
            
            seen.add(num)
            curr = num

            if curr + 1 in mapConsecutive:
                mapConsecutive[curr] = mapConsecutive[curr + 1] + 1
                continue
            
            counter = 1
            while curr + 1 in numsSet:
                counter += 1
                seen.add(curr + 1)
                curr += 1
            
            mapConsecutive[num] = counter

        return max(mapConsecutive.values())

            