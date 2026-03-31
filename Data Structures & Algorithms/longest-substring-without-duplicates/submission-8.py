class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxWindow = 0
        seen = set()

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            maxWindow = max(maxWindow, r - l + 1)
            r += 1

        return maxWindow