class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = {}
        voters = set()

        for voter, voted in trust:
            count[voted] = count.get(voted, 0) + 1
            voters.add(voter)

        for voted in count.keys():
            if count[voted] == n - 1 and voted not in voters:
                return voted
                
        return -1