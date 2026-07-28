class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        # use a monotonic stack here

        # monotonic stack is a stack that is strictly increasing or
        # strictly decreasing order at all times

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
            while stack and t > stack[-1][0]: # most recent day, last temperature
                stackT, stackInd = stack.pop() # pop from stack for both fields
                res[stackInd] = (i - stackInd) # calculate number of days gap
            stack.append([t, i]) # add both fields to the stack
        return res # return final list of daily temperatures

        # time complexity: O(n)
        # iterate through each day and temperature once

        # space complexity: O(n)
        # we use a stack, worst case scenario is every temp is
        # strictly decreasing like a [5, 4, 3, 2, 1]
        # so nothing ever gets popped and the stack grows to size n