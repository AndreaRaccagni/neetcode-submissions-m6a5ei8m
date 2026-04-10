class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        currEnd = float('-inf')
        count = 0

        for s, e in intervals:
            if s < currEnd:
                count += 1
            else:
                currEnd = e

        return count