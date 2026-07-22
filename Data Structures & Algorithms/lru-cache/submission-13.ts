class ListNode {
    key: number
    val: number
    prev: ListNode | null
    next: ListNode | null

    constructor(key: number, val: number, prev = null, next = null) {
        this.key = key
        this.val = val
        this.prev = prev
        this.next = next
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
        this.head = new ListNode(-1, -1)
        this.tail = new ListNode(-1, -1)
        this.cache = new Map()

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

        const value = node.val
        const newNode = new ListNode(key, value)
        this.remove(node)
        this.insert(newNode)

        return value
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
        this.insert(newNode)

        if (this.size > this.capacity) {
            this.remove(this.head.next)
        }
    }

    private insert(node: ListNode) {
        node.next = this.tail
        node.prev = this.tail.prev
        this.tail.prev.next = node
        this.tail.prev = node

        this.size++
        this.cache.set(node.key, node)
    }

    private remove(node: ListNode) {
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = null
        node.next = null

        this.size--
        this.cache.delete(node.key)
    }
}
