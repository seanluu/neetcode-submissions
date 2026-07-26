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

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
            