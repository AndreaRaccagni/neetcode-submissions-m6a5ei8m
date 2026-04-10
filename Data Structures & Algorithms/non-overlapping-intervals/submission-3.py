class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        curr_end = float('-inf')
        count = 0

        for s, e in intervals:
            if s < curr_end:
                count += 1
            else:
                curr_end = e

        return count