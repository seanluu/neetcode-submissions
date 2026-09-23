class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # choose the two heaviest stones, smash them together
        # since we want the heaviest stones, it makes sense to
        # use a max heap here since "heaviest" is always changing
        # with every new stone that we smash

        stones = [-s for s in stones] # sort to be in descending order from max to min

        heapq.heapify(stones) # convert max heap to an actual heap 

        while len(stones) > 1: # continue the simulation until there
        # is no more than one stone remaining
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])