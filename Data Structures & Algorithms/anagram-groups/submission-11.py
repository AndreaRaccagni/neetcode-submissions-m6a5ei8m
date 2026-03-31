class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramGroups = {}

        for s in strs:
            hashCount = [0] * 26

            for c in s:
                hashCount[ord(c) - ord('a')] += 1
            
            hashKey = tuple(hashCount)
            anagramGroups[hashKey] = anagramGroups.get(hashKey, []) + [s]

            

        return list(anagramGroups.values())