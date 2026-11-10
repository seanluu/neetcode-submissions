class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures) # autofill array with all zeroes

        # if there is no day in the future where a warmer temperature will appear for the ith day
        # rhen we set result[i] to 0 instead; use a monotonic stack here since we're strictly increasing here

        stack = []

        for i, t in enumerate(temperatures): # iterate through all indexes and values
            while stack and t > stack[-1][0]: # while stack is non-empty 
            # and our temperature t is greater than the warmest day in the future
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res