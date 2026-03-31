class MinStack {
    constructor() {
        this.stack = []
        this.min = Infinity
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val)
        this.min = Math.min(this.min, val)
    }

    /**
     * @return {void}
     */
    pop() {
        const popped = this.stack.pop()
        if (popped === this.min) {
            this.min = Math.min(...this.stack)
        }
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length - 1]
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.min
    }
}
