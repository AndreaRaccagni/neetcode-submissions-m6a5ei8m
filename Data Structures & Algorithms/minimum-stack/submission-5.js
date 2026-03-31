class MinStack {
    constructor() {
        this.stack = []
        this.minVal = []
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val)
        if (!this.minVal.length || val <= this.minVal[this.minVal.length - 1]) {
            this.minVal.push(val)
        }
    }

    /**
     * @return {void}
     */
    pop() {
        const top = this.stack.pop()
        if (top == this.minVal[this.minVal.length - 1]) {
            this.minVal.pop()
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
        return this.minVal[this.minVal.length - 1]
    }
}
