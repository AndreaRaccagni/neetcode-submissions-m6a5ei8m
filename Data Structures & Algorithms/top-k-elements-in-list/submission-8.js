class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const count = {};
        const n = nums.length

        for (const num of nums) {
            count[num] = (count[num] || 0) + 1;
        }

        const buckets = Array.from(new Array(n + 1), ()=>[])
        
        for (const [key, value] of Object.entries(count)) {
            buckets[value].push(key);
        }

        const result = buckets.reduce((acc, curr) => acc = acc.concat(curr), [])

        return result.slice(result.length - k) 
        

    }
}
