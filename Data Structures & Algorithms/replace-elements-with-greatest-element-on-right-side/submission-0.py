class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = arr[-1]

        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = currMax
            currMax = max(tmp, currMax)

        arr[-1] = -1
        return arr