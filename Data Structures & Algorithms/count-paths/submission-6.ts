class Solution {
    /**
     * @param {number} m
     * @param {number} n
     * @return {number}
     */
    uniquePaths(m: number, n: number): number {
        const arr: number[][] = Array.from({length: m}, () => new Array(n).fill(1))

        for (let r = 1; r < m; r++) {
            for (let c = 1; c < n; c++) {
                arr[r][c] = arr[r- 1][c] + arr[r][c - 1]
            }
        } 
        
        return arr[m - 1][n - 1]
    }
}
