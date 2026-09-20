class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        currMax = 0
        maxStr = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            currMax = max(count[s[r]], currMax)

            while r - l + 1 > k + currMax:
                count[s[l]] -= 1
                l += 1

            maxStr = max(maxStr, r - l + 1)
        
        return maxStr