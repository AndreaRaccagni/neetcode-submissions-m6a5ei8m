class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()
        rCanVote = 0
        dCanVote = 0
        rAlive = 0
        dAlive = 0

        for s in senate:
            if s == 'R':
                rAlive += 1
            else:
                dAlive += 1
            q.append(s)

        while True:
            candidate = q.popleft()
            if candidate == 'R':
                if dCanVote > 0:
                    dCanVote -= 1
                    rAlive -= 1
                else:
                    rCanVote += 1
                    q.append(candidate)
            else:
                if rCanVote > 0:
                    rCanVote -= 1
                    dAlive -= 1
                else:
                    dCanVote += 1
                    q.append(candidate)

            if rAlive == 0:
                return "Dire"
            elif dAlive == 0:
                return "Radiant"




