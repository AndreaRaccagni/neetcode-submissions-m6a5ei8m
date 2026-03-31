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

            if stack:
                if stack[-1] != pMap[p]:
                    return False
                else:
                    stack.pop()
            else:
                return False
                
        return len(stack) == 0