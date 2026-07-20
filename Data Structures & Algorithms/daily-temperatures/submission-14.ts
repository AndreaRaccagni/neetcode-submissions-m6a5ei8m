class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures: number[]): number[] {
        const n = temperatures.length
        const stack: number[][] = []
        const res = new Array(n).fill(0)

        for (let i = 0; i < n; i++) {
            while (stack.length && stack[stack.length - 1][0] < temperatures[i]) {
                const [t, tIndex] = stack.pop()
                res[tIndex] = i - tIndex
            }

            stack.push([temperatures[i], i])
        }

        return res
    }
}
