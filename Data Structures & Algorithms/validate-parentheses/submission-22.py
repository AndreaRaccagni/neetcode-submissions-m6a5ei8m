class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for p in s:
            if stack and p in parenthesis:
                if stack[-1] != parenthesis[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)

        return len(stack) == 0