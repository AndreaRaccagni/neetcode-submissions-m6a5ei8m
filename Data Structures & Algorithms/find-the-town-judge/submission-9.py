class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        target = trust[0][1]

        for person in trust:
            if person[1] != target:
                return -1

        return target if len(trust) < n else -1