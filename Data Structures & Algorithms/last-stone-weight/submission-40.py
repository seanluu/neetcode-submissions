class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # choose the two heaviest stones with weight x and y
        # smash together, when x == y, we destroy both
        # when x < y, we destroy x so y now has weight of y - x

        # since we want to prioritize the heaviest stones
        # and the "heaviest" is always moving
        # therefore, we should use a max heap

        stones = [-s for s in stones]

        heapq.heapify(stones) # sort into max

        while len(stones) > 1: # continue the sim until there is
        # no more than one stone remaining
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
            
        stones.append(0) # return 0 if none remain

        return abs(stones[0]) # return absolute value, since
        # we used a max heap which means the values are negative