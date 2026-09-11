class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArr = []
        p = 0
        q = 0

        while p < len(nums1) or q < len(nums2):
            v1 = float('inf') if p == len(nums1) else nums1[p]
            v2 = float('inf') if q == len(nums2) else nums2[q]

            if v1 < v2:
                mergedArr.append(v1)
                p += 1
            else:
                mergedArr.append(v2)
                q += 1

        n = len(mergedArr)
        mid = n // 2 
        if n % 2 == 0:
            return (mergedArr[mid - 1] + mergedArr[mid]) / 2
        return mergedArr[mid]