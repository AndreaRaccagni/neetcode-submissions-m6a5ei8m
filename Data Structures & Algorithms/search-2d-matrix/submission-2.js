class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        if (!matrix || !matrix[0]) return false

        const m = matrix.length
        const n = matrix[0].length
        let top = 0
        let bottom = m - 1

        while (top <= bottom) {
            const mid = parseInt((bottom - top) / 2) + top
            
            if (target < matrix[mid][0]) {
                bottom = mid - 1
            } else if (target > matrix[mid][n - 1]) {
                top = mid + 1
            } else {
                return this.binarySearch(matrix[mid], target)
            }
        }

        return false
    }

    binarySearch(arr, target) {
        let l = 0
        let r = arr.length - 1

        while (l <= r) {
            const mid = parseInt((r - l) / 2) + l
            
            if (target < arr[mid]) {
                r = mid - 1
            } else if (target > arr[mid]) {
                l = mid + 1
            } else {
                return true
            }
        }

        return false
    }
}
