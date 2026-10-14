class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []

        res = [0] * len(temperatures)

        # iterate through each index and temperature once
        for i, t in enumerate(temperatures):
            # while stack is non empty, and the current temperature is greater than temperature of the most recent waiting day

            # stack[-1] is just the pair, but stack[-1][0] is the temperature 
            # stack = [(75, 0), (71, 1), (69, 2)]
            # stack[-1]     # (69, 2)  -> last pair
            # stack[-1][0]  # 69       -> its temperature
            # stack[-1][1]  # 2        -> its index (which day it was)

            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop() # pop the temperature and index for each respective temperature
                res[stackInd] = i - stackInd # calculate number of days between curr day and next hottest day
            stack.append([t, i]) # add pair to the stack
        return res
