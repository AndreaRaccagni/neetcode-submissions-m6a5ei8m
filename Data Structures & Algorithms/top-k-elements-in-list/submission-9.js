class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        // count the occurrences
        const count = {};
        const n = nums.length;
        for (const num of nums) {
            count[num] = (count[num] || 0) + 1;
        }

        // bucket the numbers in relation to occurrences
        const buckets = Array.from(new Array(n + 1), ()=>[]);
        for (const [key, value] of Object.entries(count)) {
            buckets[value].push(key);
        }

        // find the most k elements
        let result = []
        for (let i = buckets.length - 1; i > 0; i--) {
            if (result.length < k) {
                result = result.concat(buckets[i])
            } else {
                break
            }
        }

        return result
        

    }
}
