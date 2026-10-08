class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        visiting = set()

        for crs, pre in prerequisites:
            courses[crs].append(pre)

        def dfs(course):
            if not courses[course]:
                return True

            if course in visiting:
                return False

            visiting.add(course)

            for pre in courses[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            courses[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
            
        
        return True