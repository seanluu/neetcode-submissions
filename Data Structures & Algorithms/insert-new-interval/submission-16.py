class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
        # Output: [[1,6]]

        # since the start and end interval cover [2, 5] entirely, 
        # so we use [1, 6] as the whole range
        
        res = []

        # iterate through each interval once
        for i in range(len(intervals)):
            # if new interval ends before the current interval, then we can safely add it to our output
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i::]
            # if new interval doesn't end before the current interval, then requires more work
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
        return res