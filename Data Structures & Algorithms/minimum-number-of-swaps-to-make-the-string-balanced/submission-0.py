class Solution:
    def minSwaps(self, s: str) -> int:
        maxClosing = 0
        currClosing = 0

        for b in s:
            if b == '[':
                currClosing -= 1
            else:
                currClosing += 1
                maxClosing = max(currClosing, maxClosing)

        return (maxClosing + 1) // 2


