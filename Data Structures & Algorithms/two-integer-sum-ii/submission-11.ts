class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers: number[], target: number): number[] {
        const seen: Map<number, number> = new Map()

        for (let i = 0; i < numbers.length; i++) {
            const match = target - numbers[i]

            if (seen.has(match)) {
                return [seen.get(match), i + 1]
            }
            seen.set(numbers[i], i + 1)
        }

        return [-1, -1]
    }
}
