class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        if not s:
            return count

        trimmed = s.rstrip()
        for i in range(len(trimmed) - 1, -1, -1):
            if s[i] == ' ':
                break

            count += 1

        return count