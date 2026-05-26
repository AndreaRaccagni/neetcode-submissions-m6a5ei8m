class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        const result = []

        function dfs(i, curr) {
            if (i >= nums.length) {
                result.push([...curr])
                return
            }

            curr.push(nums[i])
            dfs(i + 1, curr)

            curr.pop()
            dfs(i + 1, curr)
        }

        dfs(0, [])
        return result

    }
}
