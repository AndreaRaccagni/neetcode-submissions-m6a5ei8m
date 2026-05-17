class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        maxSize = 0
        maxFreq = 0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            maxFreq = max(maxFreq, counter[s[r]])

            while r - l + 1 > maxFreq + k:
                counter[s[l]] -= 1
                l += 1

            maxSize = max(maxSize, r - l + 1)

        return maxSize

