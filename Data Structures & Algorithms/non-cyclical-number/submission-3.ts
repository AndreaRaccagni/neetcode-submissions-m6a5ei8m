class Solution {
    /**
     * @param {number} n
     * @return {boolean}
     */
    isHappy(n: number): boolean {
        const created = new Set<number>()

        while (!created.has(n)) {
            created.add(n)
            n = this.sumOfSquares(n);

            if (n === 1) {
                return true;
            }
        }

        return false
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
