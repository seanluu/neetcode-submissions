class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # use a max heap here, since we want to choose the 2 heaviest stones
        # the heaviest is always moving
        stones = [-s for s in stones]

        heapq.heapify(stones)

        # continue the simulation until there is no more than one stone remaining
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        # return the weight of the last stone, or return 0 if none remain
        stones.append(0)
        return abs(stones[0])