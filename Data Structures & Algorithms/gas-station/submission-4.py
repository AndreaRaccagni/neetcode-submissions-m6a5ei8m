class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = sum(gas)
        totalCost = sum(cost)

        if totalCost > totalGas:
            return -1
        
        total = 0
        startingIndex = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                startingIndex = i + 1 

        return startingIndex

