class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        
        for crs, pre in prerequisites:
            courses[crs].append(pre)

        visited = set()

        def dfs(course):
            if not courses[course]:
                return True

            if course in visited:
                return False

            visited.add(course)

            for c in courses[course]:
                if not dfs(c):
                    return False
            
            visited.remove(course)
            courses[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True