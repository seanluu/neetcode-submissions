class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        path = set()

        def dfs(course):
            if course in path:
                return False
            if preMap[course] == []:
                return True

            path.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            path.remove(course)
            preMap[course] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True