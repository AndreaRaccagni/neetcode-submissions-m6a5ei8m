class Solution {
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    combinationSum2(candidates: number[], target: number): number[][] {
        candidates.sort((a, b) => a - b);
        const res: number[][] = [];

        function backtracking (i: number, curr: number[], total: number) {
            if (i > candidates.length || total > target) {
                return;
            } else if (total === target) {
                res.push([...curr]);
                return;
            }

            curr.push(candidates[i]);
            backtracking(i + 1, curr, total + candidates[i]);

            curr.pop();
            while (i + 1 < candidates.length && candidates[i] === candidates[i + 1]) {
                i++;
            }
            backtracking(i + 1, curr, total);

        }

        backtracking(0, [], 0);
        
        return res;
    }
}
