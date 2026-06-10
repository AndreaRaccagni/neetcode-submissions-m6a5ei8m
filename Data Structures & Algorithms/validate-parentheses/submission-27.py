class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in p:
                if not stack or p[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return not stack