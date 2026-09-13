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

        heapq.heapify(stones) # convert stones into a heap

        while len(stones) > 1: # continue simulation til there is no more than one stone remaining
            first = heapq.heappop(stones) # largest stone, y
            second = heapq.heappop(stones) # 2nd largest stone, x 

            if second > first: # since negated, second is less negatve, meaning x < y in real terms
                heapq.heappush(stones, first - second) # (-y) - (-x) = x - y
                # so abs() corrects it at return
            
        stones.append(0) # return 0 if no stones remain
        return abs(stones[0]) # return absolute value since we did a negation
        # to get a max heap

        # time complexity: O(n log n)
        # since each heappop and heappush is O(log n), and we do them n times
