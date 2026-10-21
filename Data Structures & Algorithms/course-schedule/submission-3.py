class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # cycle detection with DFS: you can finish every course only if the prereq
        # graph has no cycle, sort of like how you need cse 123 before 311, but if
        # 311 were also a prereq for 123 you could never take either

        preMap = {i: [] for i in range(numCourses)}  # map each course to its list of prereqs

        for course, prereq in prerequisites:
            preMap[course].append(prereq)  # build adjacency list from prerequisites

        path = set()  # courses on the current DFS path

        def dfs(course):
            if course in path:  # we looped back to a course on this path, so there's a cycle
                return False
            if preMap[course] == []:  # no prereqs left (or already proven safe)
                return True

            path.add(course)  # add course to the current path
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False  # cycle found somewhere in the prereq chain

            path.remove(course)  # done exploring from this course, so take it off the path
            preMap[course] = []  # remember this course is safe so we never re-check it
            return True  # no cycle found, course can be completed

        # check every course, since the graph might have separate pieces
        for c in range(numCourses):
            if not dfs(c):  # cycle found, so we can't complete all courses
                return False

        return True