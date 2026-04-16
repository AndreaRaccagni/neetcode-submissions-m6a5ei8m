class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+', '-', '*', '/'])
        stack = []

        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()

                stack.append(self.computeOp(a, b, t))
            else:
                stack.append(int(t))

        return stack.pop()

    
    def computeOp(self, a, b, op):
        res = 0

        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        elif op == '*':
            res = a * b
        else:
            res = math.trunc(a / b)

        return res