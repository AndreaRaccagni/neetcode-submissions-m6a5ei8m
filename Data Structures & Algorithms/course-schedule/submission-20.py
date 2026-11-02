class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)

        for crs, pre in prerequisites:
            courses[crs].append(pre)

        seen = set()

        def dfs(course):
            if not courses[course]:
                return True

            if course in seen:
                return False

            seen.add(course)

            for pre in courses[course]:
                if not dfs(pre):
                    return False

            seen.remove(course)
            courses[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True