class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for par in s:
            if par not in parenthesis:
                stack.append(par)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == parenthesis[par]:
                        stack.pop()
                    else:
                        return False

        return len(stack) == 0

        