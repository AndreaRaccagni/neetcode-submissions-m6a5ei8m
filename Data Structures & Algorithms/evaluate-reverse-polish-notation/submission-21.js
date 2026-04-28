class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const stack = []
        const ops = new Set(['+', '-', '*', '/'])

        for (const t of tokens) {
            if (!ops.has(t)) {
                stack.push(parseInt(t))
                console.log(stack)
                continue
            }

            const b = stack.pop()
            const a = stack.pop()
            let res = 0

            switch(t) {
                case '+':
                    res = a + b
                    break
                case '-':
                    res = a - b
                    break
                case '*':
                    res = a * b
                    break
                default:
                    res = Math.trunc(a / b)
            }
            stack.push(res)
        }

        return stack.pop()
    }
}
