class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const count = {}

        for (const num of nums){
            count[num] = (count[num] || 0) + 1
        }

        const countArr = new Array(nums.length + 1).fill([])

        for (const key in count){
            const index = parseInt(count[key])
            const value = parseInt(key)
            countArr[index] = countArr[index].concat([value])
        } 

        let result = []

        for (let i = countArr.length - 1; i >= 0; i--){
            if(countArr[i].length){
                result = result.concat(countArr[i])
                if(result.length === k) {
                    return result
                }
            }
        }
    }
}
