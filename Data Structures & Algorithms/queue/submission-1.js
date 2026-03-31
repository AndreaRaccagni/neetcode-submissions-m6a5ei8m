class ListNode {
    constructor(val=0, prev=null, next=null) {
        this.val = val
        this.prev = prev
        this.next = next
    }
}

class MyDeque {
    constructor() {
        this.dummyHead = new ListNode(-1)
        this.dummyTail = new ListNode(-1)

        this.dummyHead.next = this.dummyTail
        this.dummyTail.prev = this.dummyHead
    }

    /**
     * @return {boolean}
     */
    isEmpty() {
        return !this.dummyHead.next.next
    }
    /**
     * @param {number} value
     */
    append(value) {
        const node = new ListNode(value, this.dummyTail.prev, this.dummyTail)
        this.dummyTail.prev.next = node
        this.dummyTail.prev = node
    }

    /**
     * @param {number} value
     * @return {void}
     */
    appendleft(value) {    
        const node = new ListNode(value, this.dummyHead.next.prev, this.dummyHead.next)
        this.dummyHead.next.prev = node
        this.dummyHead.next = node
    }

    /**
     * @return {void}
     */
    pop() {
        if (this.isEmpty()) return -1

        const value = this.dummyTail.prev.val
        this.dummyTail.prev.prev.next = this.dummyTail.prev.next
        this.dummyTail.prev = this.dummyTail.prev.prev
        return value
    }

    /**
     * @return {number}
     */
    popleft() {
        if (this.isEmpty()) return -1

        const value = this.dummyHead.next.val
        this.dummyHead.next.next.prev = this.dummyHead.next.prev
        this.dummyHead.next = this.dummyHead.next.next
        return value
    }
}
