class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Input: piles = [1,4,3,2], h = 9
        # Output: 2

        # if we eat at rate of 1 per hour, that takes 10 hours > h = 9 so cant do that
        # if we eat at a rate of 2:

        # 1 banana = 1 hour
        # 4 bananas = 2 hours
        # 3 bananas = 2 hours, 3/2 = 1.5 rounds up since she can't switch piles mid-hour
        # 2 bananas = 1 hour
        
        l, r = 1, max(piles) # slowest possible speed, and the fastest we'd ever need (every pile done in 1 hour)

        res = r # worst case scenario

        while l <= r:
            k = l + ((r - l) // 2) # calculate midpoint 
            hours = 0
            for p in piles:
                hours += math.ceil(p / k) # round up since she can't switch piles mid-hour
            if hours <= h: # k bananas works so we try to save it and go slower
                res = k
                r = k - 1
            else:
                l = k + 1
        return res        