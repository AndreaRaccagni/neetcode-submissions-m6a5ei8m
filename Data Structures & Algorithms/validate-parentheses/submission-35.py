class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for p in s:
            if p in par:
                if not stack or par[p] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(p)

        return not stack