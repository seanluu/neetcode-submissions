class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # choose the two heaviest stones, smash them together
        # since we want the heaviest stones, it makes sense to
        # use a max heap here since "heaviest" is always changing
        # with every new stone that we smash

        stones = [-s for s in stones] # negate everything so a min-heap behaves like a max-heap

        heapq.heapify(stones) # arrange the negated list into a valid (min-)heap

        while len(stones) > 1: # continue the simulation until there
        # is no more than one stone remaining
            first = heapq.heappop(stones)   # most negative value = LARGEST real stone
            second = heapq.heappop(stones)  # next most negative value = SECOND LARGEST real stone

            # if x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x
            if second > first:
                heapq.heappush(stones, first - second) # correct in negated space: -(bigger) - (-(smaller)) = -(bigger - smaller)

        stones.append(0) # safety net: if all stones destroyed each other, stones is empty — this guarantees stones[0] exists
        return abs(stones[0]) # convert back from negated space to the real final weight (0 if none survived)

        # time complexity: O(n log n)
        # O(n) to negate + heapify initially, then up to n-1 loop iterations,
        # each doing up to 3 heap operations at O(log n) each

        # space complexity: O(n)
        # the list comprehension creates a new negated list of size n