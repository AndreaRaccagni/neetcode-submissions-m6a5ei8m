class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            first = nums[i]
            
            r = i + 1
            l = n - 1

            while r < l:
                total = nums[i] + nums[r] + nums[l]
                if total > 0:
                    l -= 1
                elif total < 0:
                    r += 1
                else:
                    result.append([nums[i], nums[r], nums[l]])
                    l -= 1
                    r += 1

                    while r < l and nums[r] == nums[r - 1]:
                        r += 1
                    while r < l and nums[l] == nums[l + 1]:
                        l -= 1
            
        return result
