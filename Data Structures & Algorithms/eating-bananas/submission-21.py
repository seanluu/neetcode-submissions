class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        res = r

        while l <= r:
            k = l + ((r - l) // 2) # k is the midpoint of the speed range
            hours = 0
            # iterate through every pile in the array piles
            for p in piles:
                hours += math.ceil(p / k) # increment number of hours and round up based on the current pile / midpoint of speed
            if hours <= h: # midpoint speed k finishes within h hours, save it and look for a slower speed that also works
                res = k 
                r = k - 1 # try a slower speed that might still work
            else:
                l = k + 1 # k is too slow, so every slower speed is too, try faster
        return res

        # tc: O(n * log m), binary search tries log m speeds (m = max(piles)),
        # and each try loops through all n piles

        # sc: O(1), no crazy data structures used here