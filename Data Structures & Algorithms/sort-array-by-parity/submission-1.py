class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        e = 0
        o = len(res) - 1

        for n in nums:
            if n % 2 == 0:
                res[e] = n
                e += 1
            else:
                res[o] = n
                o -= 1

        return res