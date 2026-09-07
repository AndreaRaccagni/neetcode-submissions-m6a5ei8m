class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        window = {}
        target = {}

        for c in t:
            target[c] = target.get(c, 0) + 1

        have = 0
        need = len(target)
        res = [-1, -1]
        minLen = float('infinity')
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in target and window[s[r]] == target[s[r]]:
                have += 1

            while have == need:
                currLen = r - l + 1
                if currLen < minLen:
                    minLen = currLen
                    res = [l, r]
                window[s[l]] -= 1

                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1

        if res[0] == -1:
            return ''

        start, end = res
        return s[start : end + 1]
