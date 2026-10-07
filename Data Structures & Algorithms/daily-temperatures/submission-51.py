class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # we use a monotonic stack here, a stack that is strictly increasing or strictly
        # decreasing order at all times

        # in this case, since we care more about the hottest day in the future,
        # we're dealing with strictly increasing 

        stack = []

        # fill array with all 0s by default
        res = [0] * len(temperatures)

        # iterate through each index and temperature once
        for i, t in enumerate(temperatures):
            # while stack is non-empty and curr temp is warmter than temp on top of the stack
            # stack holds temps in decreasing order, bottom to top)
            # t (curr temp) > stack[=1][0] (temp at top of stack, aka the more recent temp added)
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop() # pop the temperature and respective index
                res[stackInd] = i - stackInd # calculate the number of days between curr day and next highest temperature
            stack.append([t, i]) # add pair of temperature and index to the stack
            # we care more about the temperature here and returning it than the index (days), 
            # but it is still equally as important
        return res