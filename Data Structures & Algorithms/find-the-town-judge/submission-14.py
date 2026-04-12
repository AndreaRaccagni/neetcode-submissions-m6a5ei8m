class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = {}
        voters = set()
        judge = 0

        for voter, voted in trust:
            judge = voted
            voters.add(voter)
            count[voted] = count.get(voted, 0) + 1

        if len(count) == 1 and judge not in voters:
            return judge
        
        return -1
        