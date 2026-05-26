class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     * arr.toSpliced(2, 0, "Lene");
     */
    permute(nums) {
        const result = []
        const used = new Array(nums.length).fill(false)

        function dfs(curr) {
            if (curr.length == nums.length) {
                result.push([...curr])
                return
            }

            for (let i = 0; i < nums.length; i++) {
                if (used[i]) continue

                curr.push(nums[i])
                used[i] = true

                dfs(curr)

                curr.pop()
                used[i] = false
            }
        }
        dfs([])
        return result
    }
}
