class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        count = {}
        voters = set()
        judge = 0

        for voter, voted in trust:
            voters.add(voter)
            count[voted] = count.get(voted, 0) + 1

        for voted, votes in count.items():
            if votes == n - 1 and voted not in voters:
                return voted
        
        return -1
        