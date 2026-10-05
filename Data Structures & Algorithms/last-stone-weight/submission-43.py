class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones] # max heap since we want the two heaviest stones

        heapq.heapify(stones) # convert to an actual heap

        # continue the simulation until there is no more than one stone remaining
        while len(stones) > 1:
            first = heapq.heappop(stones) # first heaviest stone
            second = heapq.heappop(stones) # second heaviest stone

            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0) # return 0 if none remain

        return abs(stones[0]) # return absolute value since we used a max heap