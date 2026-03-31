class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        result = 0
        l = 0
        currMax = 0

        for r in range(len(s)):
            charMap[s[r]] = 1 + charMap.get(s[r], 0)
            currMax = max(currMax, charMap[s[r]])

            while r - l + 1 - currMax > k:
                charMap[s[l]] -= 1
                l += 1
            
            result = max(currMax, r - l + 1)

        return result 