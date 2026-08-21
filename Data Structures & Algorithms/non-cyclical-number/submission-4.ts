class Solution {
    /**
     * @param {number} n
     * @return {boolean}
     */
    isHappy(n: number): boolean {
        let slow = n;
        let fast = this.sumOfSquares(n);

        while (slow !== fast) {
            fast = this.sumOfSquares(fast);
            fast = this.sumOfSquares(fast);
            slow = this.sumOfSquares(slow);
        }

        return fast === 1;
    }

    /**
     * @param {number} n
     * @return {number}
     */
    sumOfSquares(n: number): number {
        let output = 0;

        while (n) {
            let digit = n % 10;
            output += digit * digit;
            n = Math.floor(n / 10);
        }
        return output;
    }
}
