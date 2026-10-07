class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # h = represents number of hours we have to eat all the bananas
        # k = eating rate of bananas-per-hour

        # if pile < k, we can finish eating the pile but we cannot eat from another
        # pile in the same hour

        # we want to return the minimum integer k that we can eat all the bananas within h hours

        # Input: piles = [1,4,3,2], h = 9
        # Output: 2

        # since we could have an eating rate of 2 and eat all the bananas in 9 hours

        # if we have an eating rate of 1, then it would take 10 hours
        # since 1 + 4 + 3 + 2 = 10 hours, which exceeds 9

        # however, if we have an eating rate of 2, then it would take 6 hours
        # since:
        # 1 banana = 1 hour
        # 4 bananas = 2 hours
        # 3 bananas = 2 hours
        # 2 bananas = 1 hour
        # therefore, it takes 6 hours total

        # from this, we know that we should round up hours to bananas
        # we also know to use binary search, since we want to find the exact minimum eating rate
        # in order to finish all the bananas

        l, r = 1, max(piles)

        res = r # worst case scenario: we take max amt of time to finish
        # so we have the fastest possible eating rate

        while l <= r:
            k = l + ((r - l) // 2) # calculate mid eating rate
            hours = 0

            # iterate through each pile
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
