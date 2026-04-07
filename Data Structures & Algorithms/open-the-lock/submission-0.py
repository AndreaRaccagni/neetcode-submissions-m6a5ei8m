from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"

        if start in dead:
            return -1

        q = deque([start])
        visited = {start}
        moves = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr == target:
                    return moves

                arr = list(curr)

                for i in range(4):
                    arr1 = arr.copy()
                    arr1[i] = str((int(arr1[i]) + 1) % 10)
                    nxt1 = "".join(arr1)

                    if nxt1 not in dead and nxt1 not in visited:
                        visited.add(nxt1)
                        q.append(nxt1)

                    arr2 = arr.copy()
                    arr2[i] = str((int(arr2[i]) - 1) % 10)
                    nxt2 = "".join(arr2)

                    if nxt2 not in dead and nxt2 not in visited:
                        visited.add(nxt2)
                        q.append(nxt2)

            moves += 1

        return -1