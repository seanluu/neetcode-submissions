class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y]) # since output is [[0, 2]]
            # therefore, we need to make it an array

        res = [] 
        heapq.heapify(minHeap) # convert the array into an actual heap
        # so now it's top first

        while k > 0:
            dist, x, y = heapq.heappop(minHeap) # pop every param from the heap
            res.append([x, y]) # we only want to return the x, y coords
            # we genuinely do not care about the distance
            k -= 1 # decrease the number of k closest points since
            # they're being fulfilled
        
        return res
