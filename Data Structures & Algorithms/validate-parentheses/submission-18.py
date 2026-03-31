class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for p in s:
            if p in pMap:
                if not stack or stack[-1] != pMap[p]:
                    return False
                
                stack.pop()
            else:
                stack.append(p)

        return len(stack) == 0