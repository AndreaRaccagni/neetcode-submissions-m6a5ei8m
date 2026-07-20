class MinStack {
    private stack: number[]
    private minStack: number[]

    constructor() {
        this.stack = []
        this.minStack = []
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val: number): void {
        this.stack.push(val)

        if (!this.minStack.length || val <= this.getMin()) {
            this.minStack.push(val)
        }
    }

    /**
     * @return {void}
     */
    pop(): void {
        const top = this.stack.pop()

        if (top === this.getMin()) {
            this.minStack.pop()
        }
    }

    /**
     * @return {number}
     */
    top(): number {
        return this.stack[this.stack.length - 1]
    }

    /**
     * @return {number}
     */
    getMin(): number {
        return this.minStack[this.minStack.length - 1]
    }
}
