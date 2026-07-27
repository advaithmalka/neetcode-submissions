class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if  res[-1][0] <= interval[0] <= res[-1][1] and interval[1] > res[-1][1]:
                res[-1][1] = interval[1]
            elif interval[0] > res[-1][1]:
                res.append(interval)

        return res
