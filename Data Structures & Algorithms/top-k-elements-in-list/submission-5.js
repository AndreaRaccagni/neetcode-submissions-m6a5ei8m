class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const numsOccurences = {}

        for(const num of nums){
            numsOccurences[num] = (numsOccurences[num] || 0) + 1
        }

        const counter = Array.from(new Array(nums.length + 1), () => [])

        for(const num in numsOccurences){
            counter[numsOccurences[num]].push(num)
        }

        let result = []

        for(let i = counter.length - 1; i >= 0; i--){
            if(k > result.length){
                result = result.concat(counter[i])
            } else {
                break
            }
        }

        return result
    }
}
