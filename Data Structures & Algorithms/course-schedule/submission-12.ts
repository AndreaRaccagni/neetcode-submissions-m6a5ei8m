class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses: number, prerequisites: number[][]): boolean {
        const courses: {[key: string]: number[]} = {}
        for (let i = 0; i < numCourses; i++) {
            courses[i] = []
        }

        for (const [course, prereq] of prerequisites) {
            const target = courses[course]!
            target.push(prereq)
        }

        const seen = new Set<number>()

        for (let i = 0; i < numCourses; i++) {
            if (!this.dfs(i, courses, seen)) {
                return false
            }
        }
        return true
    }

    dfs(course: number, courses: {[key: string]: number[]}, visited: Set<number>): boolean {
        if (visited.has(course)) {
            return false
        }
        if (!courses[course].length) {
            return true
        }

        visited.add(course)

        for (const c of courses[course]) {
            if (!this.dfs(c, courses, visited)) {
                return false
            }
        }

        visited.delete(course)
        courses[course] = []
        return true
    }
}
