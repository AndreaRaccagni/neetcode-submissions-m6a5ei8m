class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = Counter(arr)

        total = 0

        for n, occ in count.items():
            if n + 1 in count:
                total += occ

        return total