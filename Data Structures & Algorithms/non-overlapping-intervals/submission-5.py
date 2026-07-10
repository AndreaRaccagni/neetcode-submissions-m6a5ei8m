class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev_end = float('-inf')
        removed = 0

        for s, e in intervals:
            if s < prev_end:
                removed += 1
            else:
                prev_end = e       

        return removed
        