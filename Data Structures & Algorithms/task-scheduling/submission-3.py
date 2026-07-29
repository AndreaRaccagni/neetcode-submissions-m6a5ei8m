class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxCycle = 0
        numMaxCycles = 0

        for task, count in counter.items():
            if count > maxCycle:
                maxCycle = count
                numMaxCycles = 1
            elif count == maxCycle:
                numMaxCycles += 1

        time = (n + 1) * (maxCycle - 1) + numMaxCycles
        return max(len(tasks), time)