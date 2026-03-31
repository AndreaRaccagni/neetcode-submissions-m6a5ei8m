class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for p in s:
            if p in par:
                if not stack or stack[-1] != par[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)
        
        return len(stack) == 0

