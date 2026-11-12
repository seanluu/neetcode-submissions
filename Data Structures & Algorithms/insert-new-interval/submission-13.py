class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
        # Output: [[1,6]]

        # basically we take the lowest starting interval and the highest ending interval
        # see if it covers the new interval entirely, and return that 

        res = [] # output is an array

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i::]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)

        return res