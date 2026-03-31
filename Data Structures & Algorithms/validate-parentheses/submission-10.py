class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for p in s:
            if p in parenthesis:
                if not stack or parenthesis[p] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(p)
     
        return len(stack) == 0
