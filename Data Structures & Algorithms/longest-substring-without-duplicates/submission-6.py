class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = {}
        l = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            max_len = max(max_len, r - l + 1)

        return max_len
