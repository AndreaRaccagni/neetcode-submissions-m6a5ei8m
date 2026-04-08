class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadendsSet = set(deadends)
        start = '0000'

        if start in deadendsSet:
            return - 1
        
        count = 0
        q = deque([start])
        visited = set(start)

        while q:
            for _ in range(len(q)):
                combination = q.popleft()

                if combination == target:
                    return count

                if combination in deadendsSet:
                    continue

                for i in range(4):
                    combArr1 = list(combination)
                    combArr1[i] = str((int(combArr1[i]) + 1) % 10)
                    newComb1 = ''.join(combArr1)
                    if newComb1 not in visited:
                        visited.add(newComb1)
                        q.append(newComb1)

                    combArr2 = list(combination)
                    combArr2[i] = str((int(combArr2[i]) - 1) % 10)
                    newComb2 = ''.join(combArr2)
                    if newComb2 not in visited:
                        visited.add(newComb2)
                        q.append(newComb2)

            count += 1

        return - 1 



        