class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtracking(openP, closeP):
            if openP == closeP== n:
                res.append(''.join(curr))
                return
            
            if openP < n:
                curr.append('(')
                backtracking(openP + 1, closeP)
                curr.pop()

            if closeP < openP:
                curr.append(')')
                backtracking(openP, closeP + 1)
                curr.pop()

        backtracking(0, 0)
        return res