class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one = m - 1
        two = n - 1
        
        for i in range(m + n - 1, -1, -1):
            n1 = nums1[one] if one >= 0 else float('-inf')
            n2 = nums2[two] if two >= 0 else float('-inf')

            if n1 > n2:
                nums1[i] = n1
                one -= 1
            else:
                nums1[i] = n2
                two -= 1
