class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        currMax = -1

        for i in range(n - 1, -1, -1):
            res[i] = currMax
            currMax = max(arr[i], currMax)

        return res