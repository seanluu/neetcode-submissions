class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        # use sliding window since we need to find the minimum eating rate

        l, r = 1, max(piles)

        res = r # worst case scenario we take max amt of times to finish

        while l <= r:
            k = l + ((r - l) // 2)
            hours = 0
        
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res