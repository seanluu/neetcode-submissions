class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        # iterate through each interval in intervals
        for i in range(len(intervals)):
            # if newInterval starts after the curr interval ends
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) # add curr interval to res (since it's safely b4 newInterval)
            # if newInterval ends before curr interval starts
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval) # add it to res
                return res + intervals[i:] # and also ret res + remaining intervals 
                # (since everything after is already sorted and non-overlapping)
            # otherwise, intervals overlap so we merge by updating newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        # if loop ends, then it means newInterval belongs at the end
        res.append(newInterval)

        return res
