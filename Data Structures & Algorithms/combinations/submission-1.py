class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return

            if len(curr) + (n - i + 1) < k:
                return

            curr.append(i)
            dfs(i + 1, curr)

            curr.pop()
            dfs(i + 1, curr)


        dfs(1, [])
        return res