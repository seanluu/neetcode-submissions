class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # binary search over speeds, not over piles; we want the slowest speed that finishes in h hours
        l, r = 1, max(piles) # slowest possible speed, and fastest we'd ever need (every pile done in 1 hour)

        res = r # max(piles) always works, so it's a safe default

        while l <= r:
            k = l + ((r - l) // 2) # k is the midpoint of the speed range

            hours = 0
            # iterate through every pile in the array piles
            for p in piles:
                hours += math.ceil(p / k) # hours for this pile at speed k, round up since she can't switch piles mid-hour

            if hours <= h: # midpoint speed k finishes within h hours, save it and look for a slower speed that also works
                res = k
                r = k - 1 # slower speeds are to the left, so throw away the right side
            else:
                l = k + 1 # k is too slow, so every slower speed is too, throw away the left side and try faster

        return res # slowest speed that finished in time

        # tc: O(n * log m), binary search tries log m speeds (m = max(piles)),
        # and each try loops through all n piles

        # sc: O(1), no crazy data structures used here