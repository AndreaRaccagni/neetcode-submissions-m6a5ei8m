class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses: number, prerequisites: number[][]): boolean {
        const courses = new Map<number, number[]>()

        for (let i = 0; i < numCourses; i++) {
            courses.set(i, [])
        }

        for (const [c, prer] of prerequisites) {
            const course = courses.get(c)
            course.push(prer)
        }

        const seen = new Set();
        
        const dfs = (course: number) => {
            if (seen.has(course)) {
                return false;
            }
            if (courses.get(course).length === 0) {
                return true;
            }

            seen.add(course);
            for (let pre of courses.get(course)) {
                if (!dfs(pre)) {
                    return false;
                }
            }
            seen.delete(course);
            courses.set(course, []);
            return true;
        };

        for (let c = 0; c < numCourses; c++) {
            if (!dfs(c)) {
                return false;
            }
        }
        return true;
    }
}
