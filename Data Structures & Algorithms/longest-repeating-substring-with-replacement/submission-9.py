class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        seen = {}
        curr_max = 0
        longest = 0

        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1

            curr_max = max(curr_max, seen[s[i]])

            while (i - l + 1) - curr_max > k:
                seen[s[l]] -= 1
                l += 1

            longest = max(longest, i - l + 1)

        return longest
