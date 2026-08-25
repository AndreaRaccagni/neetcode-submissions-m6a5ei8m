class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        
        for i in range(numCourses):
            courses[i] = []

        for course, prereq in prerequisites:
            courses[course].append(prereq)

        seen = set()

        def dfs(course):
            if course in seen:
                return False
            if not courses[course]:
                return True

            seen.add(course)

            for c in courses[course]:
                if not dfs(c):
                    return False

            seen.remove(course)
            courses[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            

