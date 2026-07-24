class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix: number[][], target: number): boolean {
        let l = 0;
        let r = matrix.length - 1;

        while (l <= r) {
            const mid = Math.trunc((r - l) / 2) + l;
            const row = matrix[mid];

            if (target > row[row.length - 1]) {
                l = mid + 1;
            } else if (target < row[0]) {
                r = mid - 1;
            } else {
                return this.binarySearch(row, target);
            }
        }

        return false;
    }

    binarySearch(arr: number[], target: number): boolean {
        let l = 0;
        let r = arr.length - 1;

        while(l <= r){
            const mid = Math.trunc((r - l) / 2) + l;

            if (target > arr[mid]) {
                l = mid + 1;
            } else if (target < arr[mid]) {
                r = mid - 1;
            } else {
                return true;
            }
        }

        return false;
    }
}
