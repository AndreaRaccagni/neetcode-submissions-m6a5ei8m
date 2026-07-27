class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums: number[]): number[][] {
        const res: number[][] = []

        function dfs(i: any, curr: number[]) {
            if (i >= nums.length) {
                res.push([...curr])
                return
            }

            curr.push(nums[i])
            dfs(i + 1, curr)

            curr.pop()
            dfs(i + 1, curr)
        }
        dfs(0, [])
        return res
    }
}
