class Solution {
    /**
     * @param {number[]} nums1
     * @param {number} m
     * @param {number[]} nums2
     * @param {number} n
     * @return {void} Do not return anything, modify nums1 in-place instead.
     */
    merge(nums1: number[], m: number, nums2: number[], n: number): void {
        let one = m - 1
        let two = n - 1

        for (let i = m + n - 1; i >= 0; i--) {
            const p1 = nums1[one] ?? -Infinity
            const p2 = nums2[two] ?? -Infinity

            if (p1 > p2) {
                nums1[i] = p1
                one--
            } else {
                nums1[i] = p2
                two--
            }
        }
    }
}
