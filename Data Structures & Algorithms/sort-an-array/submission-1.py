class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        
        minNum = min(nums)
        maxNum = max(nums)
        res = []

        for n in range(minNum, maxNum + 1):
            while count.get(n) and count[n] > 0:
                res.append(n)
                count[n] -= 1
                
        return res
