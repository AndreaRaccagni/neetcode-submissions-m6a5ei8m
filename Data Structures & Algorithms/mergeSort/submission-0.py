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

    def merge(self, arr1, arr2):
        sortedArr = []
        p1, p2 = 0, 0

        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1].key <= arr2[p2].key:
                sortedArr.append(arr1[p1])
                p1 += 1
            else:
                sortedArr.append(arr2[p2])
                p2 += 1

        sortedArr.extend(arr1[p1:])
        sortedArr.extend(arr2[p2:])

        return sortedArr
