class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Use a monotonic decreasing stack.
        # Each element stores [temperature, index].
        # The stack keeps track of previous days that are
        # still waiting for a warmer temperature.
        stack = []

        # Default every answer to 0.
        # If no warmer temperature is found, the answer stays 0.
        res = [0] * len(temperatures)

        # Iterate through each day and its temperature.
        for i, t in enumerate(temperatures):

            # If the current temperature is warmer than the
            # temperature at the top of the stack, we found
            # the next warmer day for that previous day.
            #
            # Use while instead of if because the current
            # temperature could be warmer than multiple
            # previous temperatures.
            while stack and t > stack[-1][0]:

                # Remove the previous day that now has
                # its next warmer temperature.
                stackT, stackInd = stack.pop()

                # Calculate how many days we had to wait
                # from the previous day to the current day.
                res[stackInd] = i - stackInd

            # Add the current temperature and its index.
            # This day will wait for a warmer temperature
            # later in the array.
            stack.append([t, i])

        return res