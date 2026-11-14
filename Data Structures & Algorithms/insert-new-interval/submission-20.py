class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # new interval ends before this one starts, so it's entirely to the left
                # of this and everything after (list is sorted), so we're done
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # this interval ends before the new one starts, so it stays as is
                # keep looping, later intervals could still overlap
                res.append(intervals[i])
            else:
                # they overlap, so merge them into one bigger interval
                # don't add it yet, it might overlap the next one too
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # never hit the early return, so the new interval goes at the end
        res.append(newInterval)

        return res