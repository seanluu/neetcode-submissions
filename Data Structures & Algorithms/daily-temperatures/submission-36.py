class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [] # we want to return an array

        # Input: temperatures = [30,38,30,36,35,40,28]
        # Output: [1,4,1,2,1,0,0]

        # 30 < 38, 1 day
        # 38, ..., ..., ..., ..., 40, takes 4 days
        # 30 < 36, 1 day
        # 36, ... < 40, 2 days
        # 35 < 40, 1 day, 
        # 40 < never, 0 by default
        # 28 < never, 0 by default

        # we care about the value and number of days here
        # therefore it makes sense to use enumerate
        # since it can handle both

        # since we want to look for the next greater temperature
        # therefore, we should use a monontonic stack here

        stack = []

        res = [0] * len(temperatures) # autofill each element
        # in our stack with 0s, since we want to default
        # result[i] to 0 if there is no day in the future
        # where a warmer temperature will appear for the ith day
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res