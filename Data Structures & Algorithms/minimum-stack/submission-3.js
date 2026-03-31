class MinStack {
        constructor() {
        this.stack = []
        this.mins = []
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val)
        if (!this.mins.length || this.mins[this.mins.length - 1] >= val) {
            this.mins.push(val)
        }
    }

    /**
     * @return {void}
     */
    pop() {
        const popped = this.stack.pop()
        if (popped === this.mins[this.mins.length - 1]) {
            this.mins.pop()
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
        return this.mins[this.mins.length - 1]
    }
}
