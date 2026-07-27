class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        a,b = intervals[0][0], intervals[0][1]
        for i, interval in enumerate(intervals): 
            if interval[0] <= b and interval[1] >= b:
                b = interval[1]

            if interval[0] > b:
                res.append([a,b])
                a,b = interval[0], interval[1]

            if i == len(intervals) - 1:
                res.append([a,b])

        return res