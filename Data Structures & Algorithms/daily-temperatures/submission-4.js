class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const n = temperatures.length
        const stack = []
        const result = new Array(n).fill(0)

        for (let i = 0; i < n; i++) {
            while (stack.length && temperatures[i] > temperatures[stack[stack.length - 1]]) {
                const j = stack.pop()
                result[j] = i - j
            }
            stack.push(i)
        }

        return result
    }
}
