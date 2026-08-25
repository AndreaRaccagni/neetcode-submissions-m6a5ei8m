class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtracking(op, cl):
            if op == cl == n:
                res.append(''.join(curr))
                return

            if op < n:
                curr.append('(')
                backtracking(op + 1, cl)
                curr.pop()

            if cl < op:
                curr.append(')')
                backtracking(op, cl + 1)
                curr.pop()

        backtracking(0, 0)

        return res