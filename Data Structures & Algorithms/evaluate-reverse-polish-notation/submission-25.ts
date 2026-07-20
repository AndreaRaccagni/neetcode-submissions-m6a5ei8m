class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens: string[]): number {
        const stack: number[] = []
        const ops = new Set(['+', '-', '*', '/'])

        for (const t of tokens) {
            if (ops.has(t)) {
                const b = stack.pop()
                const a = stack.pop()
                let res = 0

                if (t === '+') {
                    res = a + b
                } else if (t === '-') {
                    res = a - b
                } else if (t === '*') {
                    res = a * b
                } else {
                    res = Math.trunc(a / b)
                }
                stack.push(res)
            } else {
                stack.push(Number(t))
            }
        }

        return stack.pop()
    }
}
