class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, currLen, maxLen = 0, 0, 0, 0
        seen = set()

        while end < len(s):
            if s[end] in seen:
                maxLen = max(maxLen, end - start)
                while s[end] in seen:
                    seen.discard(s[start])
                    start += 1

            seen.add(s[end])
            end += 1

        return max(maxLen, end - start)    
