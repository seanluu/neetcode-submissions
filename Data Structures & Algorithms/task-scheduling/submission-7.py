class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # each CPU cycle allows the completion of a single task, and tasks may be
        # completed in any order

        # identical tasks must be separated by at least n CPU cycles to cooldown
        # the CPU

        # return the minimum number of CPU cycles required to complete all tasks
        # mayhaps we use a min heap?

        # Input: tasks = ["X","X","Y","Y"], n = 2
        # Output: 5

        # since we can do X -> Y -> idle -> X -> Y
        # works since X always has a n = 2 gap between the next X
        # and same goes for Y

        # always run the task that has the most remaining occurrences

        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)

        time = 0

        q = deque()

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

        

        