class Node {
    /**
     * @param {number} key
     * @param {number} value
     */
    constructor(key = -1, value = -1) {
        this.key = key
        this.value = value
        this.prev = null
        this.next = null
    }
}

class LRUCache {
    /**
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = capacity
        this.cache = {}
        this.size = 0

        this.head = new Node()
        this.tail = new Node()

        this.head.next = this.tail
        this.tail.prev = this.head
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        if (this.cache[key] === undefined) {
            return -1
        }

        const node = this.cache[key]
        this.#remove(node)
        this.#insert(node)
        return node.value
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        if (this.cache[key] !== undefined) {
            this.#remove(this.cache[key])
        }
        const node = new Node(key, value)
        this.#insert(node)

        if (this.size > this.capacity) {
            const nodeToRemove = this.head.next
            this.#remove(nodeToRemove)
        }
    }

    /**
     * @param {Node} node
     * @return {void}
     */
    #insert(node) {
        node.next = this.tail
        node.prev = this.tail.prev
        node.prev.next = node
        this.tail.prev = node

        this.cache[node.key] = node
        this.size++
    }
    
    /**
     * @param {Node} node
     * @return {void}
     */
    #remove(node) {
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = null
        node.next = null

        delete this.cache[node.key]
        this.size--
    }
}
