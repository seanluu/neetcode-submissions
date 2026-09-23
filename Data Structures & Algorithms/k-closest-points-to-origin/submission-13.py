class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y]) # add all 3 params to the temp array

        res = []
        heapq.heapify(minHeap) # convert minHeap array to an actual heap
        # so the points with the closest points to origin appears first

        # while we still have k closest points to origin to fulfill...
        while k > 0: 
            dist, x, y = heapq.heappop(minHeap) # pop the closest x any y coords to the origin
            res.append([x, y]) # add said coords to the results array
            k -= 1 # decrement number of k closest points we have to fulfill
            # since we're getting closer
        
        return res

        # time complexity: O(n + k log n)
        # O(n) to build + heapify the initial heap of all points,
        # O(k log n) to pop the k closest ones (each pop is O(log n))

        # space complexity: O(n)
        # minHeap holds all n points; res holds k more (k <= n, so subsumed)
