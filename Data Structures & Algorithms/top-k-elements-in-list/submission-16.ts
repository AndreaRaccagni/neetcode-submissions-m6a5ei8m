class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const len = nums.length
        const buckets: number[][] = Array.from({length: len + 1}, () => [])
        const count: Map<number, number> = new Map()

        for (const n of nums) {
            const freq = (count.get(n) ?? 0) + 1
            count.set(n, freq)
        }

        for (const [num, freq] of count.entries()) {
            buckets[freq].push(num)
        }

        const res = []
        for (let i = len; i >= 0; i--) {
            for (const n of buckets[i]) {
                res.push(n)
                if (res.length >= k) {
                    return res
                }
            }
            
        }

        return res
    }
}
