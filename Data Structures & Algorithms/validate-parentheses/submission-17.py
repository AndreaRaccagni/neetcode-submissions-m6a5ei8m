class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for p in s:
            if p not in pMap:
                stack.append(p)
                continue

            if not stack or stack[-1] != pMap[p]:
                return False
            
            stack.pop()

        return len(stack) == 0