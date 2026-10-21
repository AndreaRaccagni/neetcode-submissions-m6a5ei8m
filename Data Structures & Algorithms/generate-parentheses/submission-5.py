class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtracking(curr, op, cl):
            if op == cl == n:
                res.append(''.join(curr))
                return

            if op < n:
                curr.append('(')
                backtracking(curr, op + 1, cl)
                curr.pop()
            
            if cl < op:
                curr.append(')')
                backtracking(curr, op, cl + 1)
                curr.pop()

        backtracking([], 0, 0)
        return res