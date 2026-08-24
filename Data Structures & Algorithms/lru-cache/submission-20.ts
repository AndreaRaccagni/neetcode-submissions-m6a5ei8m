class ListNode {
    key: number
    value: number
    prev: ListNode | null
    next: ListNode | null
    /**
     * @param {number} key
     * @param {number} value
     */
    constructor(key: number, value: number) {
        this.key = key
        this.value = value
        this.prev = null
        this.next = null
    }
}

class LRUCache {
    capacity: number
    size: number
    head: ListNode
    tail: ListNode
    cache: Map<number, ListNode>

    /**
     * @param {number} capacity
     */
    constructor(capacity: number) {
        this.capacity = capacity
        this.size = 0
        this.cache = new Map()
        this.head = new ListNode(-1, -1)
        this.tail = new ListNode(-1, -1)

        this.head.next = this.tail
        this.tail.prev = this.head
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key: number): number {
        const node = this.cache.get(key)
        if (!node) {
            return -1
        }

        this.remove(node)
        this.add(node)

        return node.value
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key: number, value: number): void {
        const node = this.cache.get(key)
        if (node) {
            this.remove(node)
        }
        const newNode = new ListNode(key, value)
        this.add(newNode)

        if (this.size > this.capacity) {
            const nodeToRemove = this.tail.prev
            this.remove(nodeToRemove)
        }
    }

    /**
     * @param {Node} node
     * @return {void}
     */
    private add(node: ListNode): void {
        node.prev = this.head
        node.next = this.head.next
        this.head.next = node
        node.next.prev = node

        this.cache.set(node.key, node)
        this.size += 1
    }

    /**
     * @param {Node} node
     * @return {void}
     */
    private remove(node: ListNode): void {
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = null
        node.next = null

        this.cache.delete(node.key)
        this.size -= 1
    }
}
