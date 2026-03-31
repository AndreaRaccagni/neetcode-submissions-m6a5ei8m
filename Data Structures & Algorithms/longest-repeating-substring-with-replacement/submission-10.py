class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqChar = 0
        l = 0
        maxChar = 0
        charMap = {}

        for r in range(len(s)):
            currChar = s[r]
            charMap[currChar] = 1 + charMap.get(currChar, 0)
            freqChar = max(freqChar, charMap[currChar])

            while r - l + 1 - freqChar > k:
                charMap[s[l]] -= 1
                l += 1

            maxChar = max(r - l + 1, maxChar)
            
        return maxChar