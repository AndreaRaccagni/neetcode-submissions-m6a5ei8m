class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_substring = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.discard(s[l])
                l += 1

            seen.add(s[r])
            max_substring = max(max_substring, r - l + 1)

        return max_substring
            