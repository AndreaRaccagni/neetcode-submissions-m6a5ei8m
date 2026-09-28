class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        q = deque()
        time = 0
        tasksMap = Counter(tasks)

        for count in tasksMap.values():
            heapq.heappush(maxHeap, -count)

        while maxHeap or q:
            time += 1
            
            if not maxHeap:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append((count, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

        

            