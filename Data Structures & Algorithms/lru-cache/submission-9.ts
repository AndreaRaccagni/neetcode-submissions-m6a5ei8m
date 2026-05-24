class ListNode {
    key: number
    value: number
    next: ListNode | null
    prev: ListNode | null

    constructor(key: number = -1, value: number = -1) {
        this.key = key
        this.value = value
        this.next = null
        this.prev = null
    }
}

class LRUCache {
    private readonly capacity: number
    private size: number
    private head: ListNode
    private tail: ListNode
    private cache: {[key: number]: ListNode}

    /**
     * @param {number} capacity
     */
    constructor(capacity: number) {
        this.capacity = capacity
        this.size = 0
        this.cache = {}

        this.head = new ListNode()
        this.tail = new ListNode()
        this.head.next = this.tail
        this.tail.prev = this.head
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key: number): number {
        if (this.cache[key] === undefined) return -1

        const nodeToUpdate = this.cache[key]
        this.remove(nodeToUpdate)
        this.insert(nodeToUpdate)
        return nodeToUpdate.value
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key: number, value: number): void {
        if (this.cache[key] !== undefined) {
            this.remove(this.cache[key])
        }

        const nodeToAdd = new ListNode(key, value)
        this.insert(nodeToAdd)

        if (this.size > this.capacity) {
            const lru = this.head.next
            this.remove(lru)
        }
    }

    /**
     * @param {ListNode} node
     * @return {void}
     */
    private insert(node: ListNode): void {
        node.prev = this.tail.prev
        node.next = this.tail
        node.prev.next = node
        this.tail.prev = node

        this.cache[node.key] = node
        this.size++
    }


    /**
     * @param {ListNode} node
     * @return {void}
     */
    private remove(node: ListNode): void {
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = null
        node.next = null

        delete this.cache[node.key]
        this.size--
    }

}
