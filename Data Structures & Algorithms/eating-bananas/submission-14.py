class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # l = 1, since eating rate cant be absolutely 0
        # r = max(piles) because if you have [1, 2, 3, 4], an eating rate of 4
        # would eat every pile in 1 hour
        l, r = 1, max(piles)

        res = r # worst case scenario we take max amt of times to finish
        # so we have the fastest possible eating rate

        # use binary search to find the exact minimum eating rate
        while l <= r:
            k = l + ((r - l) // 2) # calculate mid eating rate
            hours = 0 # track total hours needed at a rate of k
        
            # iterate through each pile at least once
            for p in piles:
                hours += math.ceil(p / k) # each pile takes ceil(p / k) hours
                # so we want to round up
            
            if hours <= h: # if k is fast enough to finish within h hours
                res = min(res, k) # k is a valid candidate, save it
                r = k - 1 # try slower rates on the left
            else:
                l = k + 1 # k too slow, try faster rates on the right
                
        return res