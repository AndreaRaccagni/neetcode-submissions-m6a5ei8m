class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        nums.sort((a: number, b: number) => a - b)
        const n = nums.length
        const res: number[][] = []

        for (let i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] === nums[i - 1]) {
                continue
            }

            let l = i + 1
            let r = n - 1

            while (l < r) {
                const s = nums[i] + nums[l] + nums[r]

                if (s > 0) {
                    r--
                } else if (s < 0) {
                    l++
                } else {
                    res.push([nums[i], nums[l], nums[r]])
                    l++
                    r--

                    while (l < r && nums[l] === nums[l - 1]) {
                        l++
                    }
                }
            }
        }

        return res
    }
}
