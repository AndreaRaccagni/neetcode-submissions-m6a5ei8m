class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(op, cl, curr):
            if op == cl == n:
                res.append(''.join(curr))
                return

            if op < n:
                curr.append('(')
                backtracking(op + 1, cl, curr)
                curr.pop()

            if cl < op:
                curr.append(')')
                backtracking(op, cl + 1, curr)
                curr.pop()

        backtracking(0, 0, [])
        return res