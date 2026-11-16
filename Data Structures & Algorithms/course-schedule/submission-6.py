class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # need to use topological sort
        
        # adjacency list
        preMap = { i: [] for i in range(numCourses)} # map each course to its prereqs

        # iterate through each course and prereq possible
        for course, prereq in prerequisites:
            preMap[course].append(prereq) # add respective prereq to each possible course we've seen so far

        visiting = set()

        def dfs(course): # explore every course to see its prereqs
            if course in visiting: # if we've seen this courses prereqs already, return False since cycle is detected
                return False

            if preMap[course] == []:
                return True

            visiting.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            preMap[course] = []

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True