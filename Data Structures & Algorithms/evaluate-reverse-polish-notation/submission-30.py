class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])

        for t in tokens:
            if t in ops:
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
                    res = math.trunc(a / b)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack[0]