class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for p in s:
            if stack and p in parenthesis:
                if parenthesis[p] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            
            stack.append(p)
        
        return len(stack) == 0
