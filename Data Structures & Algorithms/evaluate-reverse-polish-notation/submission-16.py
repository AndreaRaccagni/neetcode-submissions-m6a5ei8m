class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+', '-', '*', '/'])
        stack = []

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
                continue

            b = stack.pop()
            a = stack.pop()
            res = 0

            if t == '+':
                res = a + b
            elif t == '-':
                res = a - b
            elif t == '*':
                res = a * b
            else:
                res = int(a / b)

            stack.append(res)

        return stack.pop()