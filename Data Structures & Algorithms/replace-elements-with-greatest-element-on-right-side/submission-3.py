class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight = -1
        res = [0] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            res[i] = maxRight
            maxRight = max(maxRight, arr[i])
        
        return res