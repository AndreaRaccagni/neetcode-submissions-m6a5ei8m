class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}

        for c, pre in prerequisites:
            if c not in courses:
                courses[c] = []

            courses[c].append(pre)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if not courses.get(crs):
                return True

            visiting.add(crs)
            for pre in courses[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            del courses[crs]
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
