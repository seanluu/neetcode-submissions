class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        # [1] = last index
        # intervals is 2d, since it's essentially [start, end]
        # so intervals[i][0] is start of i-th interval
        # intervals[i][1] is the end of i-th interval
        # always read first array then second array in that order

        for i in range(len(intervals)): # iterate through each interval once
            if newInterval[1] < intervals[i][0]: # if newInterval ends before curr interval starts
            # so if we have [1, 3], [4, 6], there is no conflict, so we can add that newInterval
            # since end < start = 3 < 4
                res.append(newInterval) # add newInterval to results
                return res + intervals[i:] # return res plus the remaining intervals
                # since everything after is already sorted and non-overlapping
            elif newInterval[0] > intervals[i][1]: # if newInterval starts after curr interval ends
            # so [3, 6] > [1, 2]
            # since start > start = 3 > 1
                res.append(intervals[i]) # add curr interval to res (since it's safely before newInterval)
            else:
                newInterval = [ # otherwise, if they overlap, we merge by updating newInterval
                # example: [3, 6], [5, 8] = [3, 8] since we take lowest start, take highest end
                    min(newInterval[0], intervals[i][0]), # so newInterval.start = min
                    max(newInterval[1], intervals[i][1]), # newInterval.end = max
                ]
        res.append(newInterval) # if loop ends, newInterval belongs at the end
        # so we can add newInterval to the results array
        return res # return all intervals

        # time complexity: O(n)
        # since we iterate through each interval once

        # space complexity: O(1)
        # no crazy data structures used