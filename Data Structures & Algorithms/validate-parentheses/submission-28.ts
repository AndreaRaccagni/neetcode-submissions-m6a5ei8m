class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        const stack = []
        const par = {
            ')': '(',
            ']': '[',
            '}': '{'       
            }

        for (const p of s) {
            if (p in par) {
                if (stack.length && stack[stack.length - 1] === par[p]) {
                    stack.pop()
                } else {
                    return false
                }
            } else {
                stack.push(p)
            }
        }

        return stack.length === 0
    }
}
