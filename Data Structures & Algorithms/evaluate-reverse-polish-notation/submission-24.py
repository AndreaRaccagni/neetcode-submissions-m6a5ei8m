class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
                continue

            n = 0
            b = stack.pop()
            a = stack.pop()

            if t == '+':
                n = a + b
            elif t == '-':
                n = a - b
            elif t == '*':
                n = a * b
            else:
                n = math.trunc(a / b)

            stack.append(n)
        
        return stack.pop()