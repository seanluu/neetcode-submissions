class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = { i: [] for i in range(numCourses) } 

        for course, prereq in prerequisites:
            preMap[course].append(prereq) # build adjacency list from prerequisites

        visit = set()

        def dfs(course):
            if course in visit: # if we already saw this course in path, cycle is detected
                return False
            if preMap[course] == []: # otherwise if we don't have any prereqs left, course is safe to take
                return True

            visit.add(course) # mark course as visited in our curr path
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False # cycle found in prereq chain
            
            visit.remove(course) # rdone with this path so we unmark th course
            preMap[course] = [] # optimization since we no longer need to revisit this course again
            return True # no cycle found, course can be completed

        # iterate through each course
        for c in range(numCourses):
            if not dfs(c): # cycle found so we can't complete all courses
                return False
        
        return True