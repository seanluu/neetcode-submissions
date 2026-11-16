"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

    # Input: intervals = [(0,40),(5,10),(15,20)]
    # Output: 2

    # r1: (0, 40)
    # r2: (5, 10), (15, 20)

    # we separate them into two separate rooms since if we were to include (0, 40), 
    # then it overlaps while (5, 10) and (15, 20) are still ongoing.
    # (5, 10) and (15, 20) can use the same room since (5, 10) ends before (15, 20)

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted(i.start for i in intervals) # sort start dates for all our intervals
        end = sorted(i.end for i in intervals) # sort end dates for all our intervals

        res, count = 0, 0 # output is an integer
        # count is necessary for keeping track of all the active meetings at the moment

        s, e = 0, 0 # left, right pointers?

        while (s < len(intervals)):
            # if start time is less than the end time
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)

        return res
                


            