class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for op in operations:
            if op == 'C':
                total -= stack.pop()
                continue
            elif op == '+':
                score = stack[-1] + stack[-2]
            elif op == 'D':
                score = stack[-1] * 2
            else:
                score = int(op)

            stack.append(score)
            total += score

        return total