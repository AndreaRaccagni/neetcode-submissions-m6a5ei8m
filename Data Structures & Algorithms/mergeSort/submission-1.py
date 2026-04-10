# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) < 2:
            return pairs

        mid = len(pairs) // 2

        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        merged = []
        l = 0
        r = 0

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
        
        merged.extend(left[l:])
        merged.extend(right[r:])
        return merged

