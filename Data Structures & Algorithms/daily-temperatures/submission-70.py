class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        # monotonic stack: keeps elements in sorted order by popping anything
        # that would break the order before pushing

        # here the stack is non-increasing (bottom to top): we pop any waiting day
        # that's cooler than today, since today is its next warmer day

        # as we iterate through the array, before pushing a new element
        # we pop off anything that would breka that order, so the order
        # stays sorted in one direction

        # in this case, we want an increasing stack where we scan
        # from left to right since we want to find the next day
        # with a higher temperature

        res = [0] * len(temperatures) 
        # fill array with all 0s by default
        # to cover the case where there is no day in the future
        # where a warmer temperture will appear for the ith day
        # and we want to set the result[i] to 0

        # iterate through num of days and actual temperatures
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # today is warmer than the most recent waiting day
                stackT, stackInd = stack.pop() # pop from stack for both fields
                res[stackInd] = (i - stackInd) # calculate number of days gap
            stack.append([t, i]) # add both fields to the stack
        return res # number of days each day waits for a warmer one

        # time: O(n), each day is pushed once and popped at most once,
        # so the inner while loop does O(n) total work across the whole run

        # space complexity: O(n)
        # we use a stack, worst case scenario is every temp is
        # strictly decreasing like a [5, 4, 3, 2, 1]
        # so nothing ever gets popped and the stack grows to size n