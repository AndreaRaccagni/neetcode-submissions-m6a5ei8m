/**
 * Singly Linked List Node
 */
class ListNode {
    /**
     * @param {number} val - Value of the node
     * @param {ListNode} [nextNode=null] - Reference to the next node
     */
    constructor(val = -1, nextNode = null) {
        this.val = val;
        this.next = nextNode;
    }
}

class LinkedList {
    constructor(val = 0, next = null) {
        this.head = new ListNode();
        this.tail = this.head;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        let curr = this.head.next;
        let i = 0;
        while (curr) {
            if (i === index) {
                return curr.val
            }
            curr = curr.next;
            i++;
        }

        return -1
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        const node = new ListNode(val)   
        node.next = this.head.next;
        this.head.next = node;
        if(!node.next) {
            this.tail = node;
        }

    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        const node = new ListNode(val)
        this.tail.next = node;
        this.tail = this.tail.next;
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        let i = 0;
        let curr = this.head;
        while (i < index && curr) {
            i++;
            curr = curr.next;
        }

        if (curr && curr.next) {
            if (curr.next === this.tail) {
                this.tail = curr;
            }
            curr.next = curr.next.next;
            return true;
        }
        return false;
    }

    /**
     * @return {number[]}
     */
    getValues() {
        let curr = this.head.next;
        const values = [];
        while (curr) {
            values.push(curr.val)
            curr = curr.next;
        }

        return values;
    }
}
