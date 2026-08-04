class TimeMap {
    keyStore: Map<string, { timestamp: number, value: string }[]>

    constructor() {
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key: string, value: string, timestamp: number): void {
        if (!this.keyStore.has(key)) {
            this.keyStore.set(key, [])
        }
        const values = this.keyStore.get(key)
        values.push({ timestamp, value })
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key: string, timestamp: number): string {
        const currValues = this.keyStore.get(key)
        if (!currValues || !currValues.length) {
            return ''
        }
        
        return this.getValue(currValues, timestamp)

    }

    private getValue(values: { timestamp: number, value: string }[], timestamp: number): string {
        let l = 0
        let r = values.length - 1
        let target = -1

        while (l <= r) {
            const mid = Math.floor((r - l) / 2) + l

            if (values[mid].timestamp === timestamp) {
                return values[mid].value
            } else if (timestamp < values[mid].timestamp) {
                r = mid - 1

            } else {
                target = mid
                l = mid + 1
            }
        }
        return target !== -1 ? values[target].value : ''
    }
}
