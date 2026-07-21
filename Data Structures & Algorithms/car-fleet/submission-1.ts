class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target: number, position: number[], speed: number[]): number {
        const cars: number[][] = []

        for (let i = 0; i < position.length; i++) {
            cars.push([position[i], speed[i]])
        }

        cars.sort((a: number[], b: number[]) => b[0] - a[0])

        let fleets = 0
        let hrsFleet = -Infinity
        for (const [pos, carSpeed] of cars) {
            const hrs = (target - pos) / carSpeed
            if (hrs > hrsFleet) {
                fleets++
                hrsFleet = hrs
            }
        }
 
        return fleets
    }
}
