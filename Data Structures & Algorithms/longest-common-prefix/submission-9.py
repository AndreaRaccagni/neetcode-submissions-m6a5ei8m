class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            minLen = min(len(strs[i]), len(prefix))
            for j in range(minLen):
                if prefix[j] != strs[i][j]:
                    prefix = prefix[:j]
                    break
            
            prefix = prefix[:minLen]

        return prefix or ''