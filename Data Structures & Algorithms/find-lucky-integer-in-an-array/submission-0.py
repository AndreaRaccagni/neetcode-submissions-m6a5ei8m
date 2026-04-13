class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)

        lucky = -1
        for n, occ in count.items():
            if n == occ:
                lucky = max(lucky, n)

        return lucky