class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        stack = []

        for c in s:
            if c == '(':
                stack.append(c)
                depth = max(depth, len(stack))
            elif c == ')':
                stack.pop()

        return depth