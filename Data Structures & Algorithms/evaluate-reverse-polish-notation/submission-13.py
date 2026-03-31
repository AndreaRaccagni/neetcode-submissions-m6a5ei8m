class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set(['*', '+', '-', '/'])

        for t in tokens:
            nextNum = 0
            if t in operations:
                b = stack.pop()
                a = stack.pop()
                if t == '*':
                    nextNum = a * b
                elif t == '+':
                    nextNum = a + b
                elif t == '-':
                    nextNum = a - b
                else:
                    nextNum = int(a / b)
            else:
                nextNum = int(t)

            stack.append(nextNum)

        return stack[0]