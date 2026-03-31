class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.list = []
        this.capacity = capacity 
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.list[i]
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.list[i] = n
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        if(this.capacity === this.list.length){
           this.resize() 
        }
        this.list.push(n)
    }

    /**
     * @returns {number}
     */
    popback() {
        return this.list.pop()
    }

    /**
     * @returns {void}
     */
    resize() {
        this.capacity *= 2
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.list.length
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity
    }
}
