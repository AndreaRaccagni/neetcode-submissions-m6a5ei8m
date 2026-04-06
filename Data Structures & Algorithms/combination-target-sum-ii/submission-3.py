class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def combine(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            
            if total > target or i == len(candidates):
                return

            curr.append(candidates[i])
            combine(i + 1, curr, total + candidates[i])
            curr.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1

            combine(i + 1, curr, total)


        combine(0, [], 0)
        return result