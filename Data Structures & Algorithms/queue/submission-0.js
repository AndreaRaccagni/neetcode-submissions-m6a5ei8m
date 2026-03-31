class MyDeque {
    constructor() {
        this.deque = []
    }

    /**
     * @return {boolean}
     */
    isEmpty() {
        return this.deque.length === 0
    }

    /**
     * @param {number} value
     */
    append(value) {
        this.deque.push(value)
    }

    /**
     * @param {number} value
     * @return {void}
     */
    appendleft(value) {
        this.deque.unshift(value)
    }

    /**
     * @return {void}
     */
    pop() {
        return this.isEmpty() ? -1 : this.deque.pop()
    }

    /**
     * @return {number}
     */
    popleft() {
        return this.isEmpty() ? -1 : this.deque.shift()
    }
}
