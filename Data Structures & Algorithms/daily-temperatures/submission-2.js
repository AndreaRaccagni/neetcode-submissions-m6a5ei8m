class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        const stack = [] //item: [temperature, index]
        const days = new Array(temperatures.length).fill(0)

        for (let i = 0; i < temperatures.length; i++) {
            while (stack.length && temperatures[i] > stack[stack.length - 1][0]) {
                const popped = stack.pop()
                days[popped[1]] = i - popped[1]
            }
            stack.push([temperatures[i], i])
        }

        return days
    }
}
