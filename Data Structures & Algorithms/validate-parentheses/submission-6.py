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
                if stack and stack[-1] == par[p]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(p)
        
        return len(stack) == 0

