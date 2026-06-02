class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}

        for c, pre in prerequisites:
            if c not in courses:
                courses[c] = []

            courses[c].append(pre)

        visiting = set()

        def dfs(curr):
            if curr in visiting:
                return False
            if not courses.get(curr):
                return True

            visiting.add(curr)
            for pre in courses[curr]:
                if not dfs(pre):
                    return False
            visiting.remove(curr)
            return True

        for c in courses.keys():
            if not dfs(c):
                return False

        return True