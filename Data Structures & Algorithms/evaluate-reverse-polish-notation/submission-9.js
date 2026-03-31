class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const stack = []
        const operators = new Set(['+', '-', '*', '/'])

        for (const token of tokens) {
            if (operators.has(token)) {
                const num2 = stack.pop()
                const num1 = stack.pop()
                let tmp = 0

                if (token === '+') {
                    tmp = num1 + num2
                } else if (token === '-') {
                    tmp = num1 - num2
                } else if (token === '*') {
                    tmp = num1 * num2
                } else {
                    tmp = Math.trunc(num1 / num2)
                }
                stack.push(parseInt(tmp))

            } else {
                stack.push(parseInt(token))
            }
        }
        return stack.pop()
    }
}
