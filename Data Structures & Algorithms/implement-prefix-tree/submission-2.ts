class TrieNode {
    chars: Array<TrieNode | null>
    endOfWord: boolean
    
    constructor() {
        this.chars = new Array(26).fill(null)
        this.endOfWord = false
    }
}

class PrefixTree {
    root: TrieNode

    constructor() {
        this.root = new TrieNode()
    }

    /**
     * @param {string} word
     * @return {void}
     */
    insert(word: string): void {
        let p = this.root
        for (const w of word) {
            const index = w.charCodeAt(0) - 'a'.charCodeAt(0)
            if (!p.chars[index]) {
                p.chars[index] = new TrieNode()
            }
            p = p.chars[index]
        }
        p.endOfWord = true
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word: string): boolean {
        let p = this.root
        for (const w of word) {
            const index = w.charCodeAt(0) - 'a'.charCodeAt(0)
            if (!p.chars[index]) {
                return false
            }
            p = p.chars[index]
        }
        return p.endOfWord
    }

    /**
     * @param {string} prefix
     * @return {boolean}
     */
    startsWith(prefix: string): boolean {
        let p = this.root
        for (const w of prefix) {
            const index = w.charCodeAt(0) - 'a'.charCodeAt(0)
            if (!p.chars[index]) {
                return false
            }
            p = p.chars[index]
        }
        return true
    }
}
