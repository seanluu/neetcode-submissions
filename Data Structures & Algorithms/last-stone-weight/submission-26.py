class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # choose the two heaviest stones with weight x and y

        # if x == y, we destroy both stones -> pop

        # if x < y, we get rid of x, then y = y - x

        # since we want to choose the heaviest stones, therefore
        # it makes sense to use a max heap

        # reminder to self that heap isn't ordered
        # but the first element should be the max element

        # so it just makes sense to do a max heap twice to get 
        # the two heaviest stones

        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
            
        stones.append(0)
        return abs(stones[0])
