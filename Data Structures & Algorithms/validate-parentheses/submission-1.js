class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = []
        const parenthesis = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for (const p of s){
            if(p in parenthesis){
                if(stack.length === 0 || stack[stack.length - 1] !== parenthesis[p]){
                    return false
                }
                stack.pop()
            } else {
                stack.push(p)
            }
        }

        return stack.length === 0
    }
}
