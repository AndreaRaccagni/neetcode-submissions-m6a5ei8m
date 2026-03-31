class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for op in operations:

            if op == 'C':
                removed = stack.pop()
                total -= removed

            elif op == '+':
                nextScore = stack[-1] + stack[-2]
                stack.append(nextScore)
                total += nextScore

            elif op == 'D':
                nextScore = stack[-1] * 2
                stack.append(nextScore)
                total += nextScore

            else:
                nextScore = int(op)
                stack.append(nextScore)
                total += nextScore

        return total