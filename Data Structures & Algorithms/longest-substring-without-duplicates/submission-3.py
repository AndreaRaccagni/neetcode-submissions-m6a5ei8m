class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, maxLen = 0, 0
        seen = set()

        for i in range(len(s)):
            while s[i] in seen:
                seen.discard(s[start])
                start += 1
            seen.add(s[i])
            maxLen = max(maxLen, i - start + 1)

        return maxLen
