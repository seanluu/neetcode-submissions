class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # return the k closest points to the origin (0, 0)
        # since we are working with "k", this tells us that
        # we should use a heap here

        # since we want closest points to the origin, it makes
        # most sense to use a minHeap here

        # we're also working with coordinates, so only makes
        # sense to use x, y coords

        minHeap = []

        # iterate through each x and y coord in the points
        for x, y in points:
            dist = (x ** 2) + (y ** 2) # calculate the distance
            minHeap.append([dist, x, y]) # add this point's [distance, x, y]

        heapq.heapify(minHeap) # heapify AFTER all points are added, not before

        res = []

        while k > 0: # while there are still k closest points to handle
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y]) # add only the points to results,
            # since our goal isn't to return the distance
            k -= 1 # decrement the number of k since we just satisfied it
        return res # return final list of k closest points to the origin