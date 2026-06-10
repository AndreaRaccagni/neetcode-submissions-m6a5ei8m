class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if stack and c in p:
                if p[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0