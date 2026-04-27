# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        mid = len(pairs) // 2

        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])

        return self.merge(left, right)


    def merge(self, left, right):
        l = 0
        r = 0
        curr = 0
        res = [None] * (len(left) + len(right))
        
        while curr < len(res):
            leftVal = left[l].key if l < len(left) else float('inf')
            rightVal = right[r].key if r < len(right) else float('inf')
            
            if leftVal <= rightVal:
                res[curr] = left[l]
                l += 1
            else:
                res[curr] = right[r]
                r += 1
            curr += 1

        return res
        
