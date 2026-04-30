class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        currStart = intervals[0][0]
        currEnd = intervals[0][1]
        res = []

        for start, end in intervals:
            if start > currEnd:
                res.append([currStart, currEnd])
                currStart = start
                currEnd = end
            else:
                currEnd = max(currEnd, end)
        res.append([currStart, currEnd])
        return res